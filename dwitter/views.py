from django.shortcuts import render,redirect
from .models import Profile,Account,User,Dweet,Comment
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from django.urls import reverse,reverse_lazy
from django.shortcuts import get_object_or_404

@login_required
def dashboard( request):

    return render(request, "dwitter/dashboard.html")

# すべて表示
@login_required
def profile_list(request):
    
        if 'q' in request.GET:
            q = request.GET['q']
            
            multiple_q = Q(Q(user__username__icontains=q) | Q(age__icontains=q) | Q(hobby__icontains=q)| Q(last_name__icontains=q)| Q(area__icontains=q))
            account = Account.objects.filter(multiple_q)
        else:
            account = Account.objects.exclude(user=request.user)
        context = {
            'account': account
        }
        return render(request, "dwitter/profile_list.html", context)

# フォローを表示
@login_required
def profile(request, pk):
    # プロファイルを作成していない場合はRelatedObjectDoesNotExistの対策
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()


    profile = Profile.objects.get(pk=pk)
    # followボタンが押されたら発生
    if request.method == "POST":
        # ログインユーザーを参照
        current_user_profile = request.user.profile
        # valueの値をdataに入れる
        data = request.POST

        action = data.get("follow")
        # 押されたボタンによって追加か削除をする
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})

class UserView(LoginRequiredMixin, DetailView):
    template_name = 'dwitter/message.html'
    model = Profile

class UserCreate(LoginRequiredMixin, CreateView):
    template_name = 'dwitter/create.html'
    model = Dweet
    fields = ('body',)
    def get_success_url(self):
        return reverse('UserView', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        """投稿ユーザーをリクエストユーザーと紐付け"""
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserDelete(LoginRequiredMixin, DeleteView):
    template_name = 'dwitter/delete.html'
    model = Dweet
    success_url = reverse_lazy('dashboard')


class UserUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'dwitter/update.html'
    model = Dweet
    fields = ('body',)
    success_url = reverse_lazy('dashboard')

class CommentView(LoginRequiredMixin, DetailView):
    template_name = 'dwitter/comment.html'
    model = Dweet

    def get_context_data(self, **kwargs):
        context = super(CommentView, self).get_context_data(**kwargs)
        context.update({
            'comment': Comment.objects.all(),
        })
        return context

class CommentCreate(LoginRequiredMixin, CreateView):
    template_name = 'dwitter/commentCreate.html'
    model = Comment
    fields = ('body',)

    def form_valid(self, form):
        post_pk = self.kwargs['pk']
        post = get_object_or_404(Dweet, pk=post_pk)
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.dweet = post
        comment.save()
        return redirect('comment',  pk=post_pk)

class CommentDelete(LoginRequiredMixin, DeleteView):
    template_name = 'dwitter/delete.html'
    model = Comment
    success_url = reverse_lazy('dashboard')


class CommentUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'dwitter/update.html'
    model = Comment
    fields = ('body',)
    success_url = reverse_lazy('dashboard')
