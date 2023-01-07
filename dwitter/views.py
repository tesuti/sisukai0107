from django.shortcuts import render
from .models import Profile,Account,User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
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

class DetailUserView( DetailView):
    template_name = 'dwitter/profile.html'
    model = User