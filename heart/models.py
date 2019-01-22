from django.db import models
from django.utils.timezone import datetime
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
# -*- coding: utf-8 -*-
class User(models.Model):
    name= models.CharField(max_length=20)#사용자의 이름
    nickName=models.CharField(max_length=20)#사용자가 설정한 닉네임
    studentId=models.PositiveIntegerField()#학번;
    sex=models.CharField(max_length=1)#성별; 남자 : M, 여자 : F
    birthDate=models.DateField()#생일; 형식 : 1995-09-30
    signInDate=models.DateTimeField(auto_now_add=True)#가입 날짜; 형식 : 2018-01-17 
    icon=models.ImageField()#사용자가 가입할 때 선택할 수 있는 아이콘
    phone=models.CharField(max_length=15, default=None)#핸드폰 번호; 형식: xxx-xxxx-xxxx
    # blockUser=ListCharField(
    #     base_field=IntegerField(max_length=10),
    #     size=100,
    #     max_length=(7 * 100),
    #     blank=True
    # )
    # 사용자가 차단한 유저의 정보; pk로 저장하고 최대치는 100명으로 설정함
    resign=models.BooleanField(default=False)#탈퇴 날짜
    email=models.EmailField(default=None)#사용자의 이메일 정보

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False) 
    content = models.CharField(max_length=3000, blank= True)
    postEditor =  RichTextUploadingField(blank=True, null=True,
                                          external_plugin_resources=[(
                                          'youtube',
                                          '/static/heart/external/ckeditor_plugins/youtube/youtube/',
                                          'plugin.js',
                                          )],
                                      )
    pubDate = models.DateTimeField(auto_now_add=True, blank=False) 
    updateDate = models.DateTimeField(auto_now_add=True, blank=True) 
    hitCount = models.PositiveIntegerField(default=0) #조회수
    boardNum = models.PositiveIntegerField(blank=False) #게시판 별 고유번호
    reportStatus = models.CharField(max_length=10, blank=True) # mypage-신고내역 ( 미확인, 확인중, 확인완료 )
    status = models.CharField(max_length=10, blank=True)  # lostNfound, 한동장터 ( 판매중, 판매완료, Lost, Found, 해결완료 )
    boardType = models.CharField(max_length=10, blank=True) # lostNfound, 한동장터 ( 팝니다, 삽니다, Lost, Found )
    itemType = models.CharField(max_length=10, blank=True) #lostNfound, 한동장터 ( 태그 )
    price = models.CharField(max_length=100, blank=True) 
    exist = models.BooleanField(default=True) # 삭제 여부
    users = models.ManyToManyField(
      User,
      through = 'PostRelation',
      through_fields = ('post', 'user'),
    )

    def __str__(self):
        return self.title
    
    def update_hitCount(self):
        self.hitCount += 1
        self.save()


class Comment(models.Model):
    title = models.CharField(max_length=100, blank=True)  #활주로에서 댓글이 게시글 형식으로 달릴 때 필요    
    users = models.ManyToManyField(
        User, 
        through='ComRelation',
        through_fields=('comment', 'user'))  #댓글과 관련된 유저들
    pubDate = models.DateTimeField(auto_now_add=True) #댓글 생성날짜
    content = models.TextField(max_length=3000, blank=True) #댓글 내용
    commentEditor = RichTextUploadingField(blank=True, null=True, config_name='comment')
    belongToBoard = models.PositiveIntegerField(blank= True) #어떤 게시판에 소속된 댓글인지 알 수 있도록 게시판의 pk표시
    belongToComment = models.PositiveIntegerField(blank= True) #어떤 댓글에 소속된 대댓글인지 알 수 있도록 상위 댓글의 pk표시
    stance = models.PositiveIntegerField(blank= True) #활주로에서 댓글의 의견 상태 표시 0:반대 1:찬성 2:중립
    reportStatus = models.CharField(max_length=10,blank= True) #신고 상태
    noticeChecked = models.BooleanField(default=False) #알림을 확인 했는지 표시

    def __str__(self):
        return self.title

class File(models.Model):
    belongTo = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

class PostRelation(models.Model):
    annonimity=models.BooleanField(default=False)
    annoName=models.CharField(max_length=20, blank= True)
    isWriter=models.BooleanField(default=False)
    like=models.BooleanField(default=False)
    dislike=models.BooleanField(default=False)
    vote=models.PositiveIntegerField(default=0, blank= True) #각 게시물 detailview에서 내가 투표한 결과를 볼 수 있게
    user = models.ForeignKey(User, related_name = 'post_relation',on_delete=models.CASCADE)#user로 연결되는 foreignkey
    post = models.ForeignKey(Post, related_name = 'post_relation', on_delete=models.CASCADE)#post로 연결되는 foreignkey

class ComRelation(models.Model):
    annonimity=models.BooleanField(default=False)
    annoName=models.CharField(max_length=20, blank= True)
    isWriter=models.BooleanField(default=False)
    like=models.BooleanField(default=False)
    dislike=models.BooleanField(default=False)
    vote=models.PositiveIntegerField(blank= True) #각 게시물 detailview에서 내가 투표한 결과를 볼 수 있게
    user = models.ForeignKey(User, related_name = 'com_relation', on_delete=models.CASCADE)#user로 연결되는 foreignkey
    comment = models.ForeignKey(Comment, related_name = 'com_relation', on_delete=models.CASCADE)#comment로 연결되는 foreignkey
