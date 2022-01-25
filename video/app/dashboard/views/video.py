# -*- coding:utf-8 -*-

from django.template.base import kwarg_re
from django.views import View
from django.shortcuts import redirect, reverse
from app.libs.base_mako import render_to_response
from app.utils.permission import dashboard_auth
from app.model.video import VideoType, FromType, NationalityType, IdentityType
from app.model.comment import Comment
from app.utils.common import check_and_get_video_type, handle_video
from app.model.video import Video, VideoSub, VideoStar

class ExternalVideo(View):
    TEMPLATE = 'dashboard/video/external_video.html'
    
    @dashboard_auth
    def get(self, request):
        data = {}
        error = request.GET.get('error', '')
        data['error'] = error
        
        cus_videos = Video.objects.filter(from_to=FromType.custom.value)
        ex_videos = Video.objects.exclude(from_to=FromType.custom.value)
        data['ex_videos'] = ex_videos
        data['cus_videos'] = cus_videos
        
        return render_to_response(request, self.TEMPLATE, data)

    def post(self, request):
        name = request.POST.get('name')
        image = request.POST.get('image')
        video_type = request.POST.get('video_type')
        from_to = request.POST.get('from_to')
        nationality = request.POST.get('nationality')
        info = request.POST.get('info')
        video_id = request.POST.get('video_id')
        
        if video_id:
            reverse_path = reverse('dashboard_externalvideo_update', kwargs={'video_id': video_id})
        else:
            reverse_path = reverse('dashboard_externalvideo')
        
        if not all([name, image, video_type, from_to, nationality, info]):
            return redirect('{}?error={}'.format(reverse_path, '缺少必要信息'))
        
        result = check_and_get_video_type(VideoType, video_type, '非法的视频类型')
        if result.get('code') != 0 :
            return redirect('{}?error={}'.format(reverse_path, result.message))
        
        result = check_and_get_video_type(FromType, from_to, '非法的视频来源')
        if result.get('code') != 0 :
            return redirect('{}?error={}'.format(reverse_path, result.message))
        
        result = check_and_get_video_type(NationalityType, nationality, '该国家未收录')
        if result.get('code') != 0 :
            return redirect('{}?error={}'.format(reverse_path, result.message))
        
        if not video_id:
            try:
                Video.objects.create(
                    name=name,
                    image=image,
                    video_type=video_type,
                    from_to=from_to,
                    nationality=nationality,
                    info=info
                )
            except:
                return redirect('{}?error={}'.format(reverse_path, '创建失败'))
            
        else:
            try:
                video = Video.objects.get(id=video_id)
                video.name = name
                video.image = image
                video.video_type = video_type
                video.from_to = from_to
                video.nationality = nationality
                video.info = info
                video.save()
            except:
                return redirect('{}?error={}'.format(reverse_path, '修改失败'))
            
        
        return redirect(reverse('dashboard_externalvideo'))

class VideoSubView(View):
    TEMPLATE = 'dashboard/video/videosub.html'
    
    @dashboard_auth
    def get(self, request, video_id):
        data = {}
        video = Video.objects.get(id=video_id)
        data['video'] = video
        error = request.GET.get('error', '')
        data['error'] = error
        
        comments = Comment.objects.filter(video=video).order_by('-id')
        data['comments'] = comments
        return render_to_response(request, self.TEMPLATE, data)
    
    def post(self, request, video_id):
        data = {}
        number = request.POST.get('number')
        videosub_id = request.POST.get('videosub_id')
        
        video = Video.objects.get(id=video_id)
        
        if FromType(video.from_to) == FromType.custom:
            url = request.FILES.get('url')
        else:
            url = request.POST.get('url')
            
        data['url'] = url
        
        if not all([url, number]):
            return redirect('{}?error={}'.format(reverse('dashboard_videosub', kwargs = {'video_id': video_id}), '缺少信息'))
        
        if FromType(video.from_to) == FromType.custom:
            handle_video(url, video_id, number)
            return redirect(reverse('dashboard_videosub', kwargs = {'video_id': video_id}))
            
        
        if not videosub_id:
            try:
                VideoSub.objects.create(
                    video = video,
                    url = url,
                    number = number,
                )
            except:
                return redirect('{}?error={}'.format(reverse('dashboard_videosub', kwargs = {'video_id': video_id}), '创建失败'))
        
        else:
            try:
                videosub = VideoSub.objects.get(id=videosub_id)
                videosub.url = url
                videosub.number = number
                videosub.save()
            except:
                return redirect('{}?error={}'.format(reverse('dashboard_videosub', kwargs = {'video_id': video_id}), '修改失败'))
            
        return redirect(reverse('dashboard_videosub', kwargs = {'video_id': video_id}))
        
class VideoStarView(View):
    def post(self, request):
        name = request.POST.get('name')
        identity = request.POST.get('identity')
        video_id = request.POST.get('video_id')
        star_id = request.POST.get('star_id')
        
        
        if not all([name, video_id, identity]):
            return redirect('{}?error={}'.format(reverse('dashboard_videosub', kwargs = {'video_id': video_id}), '缺少必要信息'))
            
        result = check_and_get_video_type(IdentityType, identity, '该身份未收录')
        if result.get('code') != 0 :
            return redirect('{}?error={}'.format(reverse('dashboard_videosub', kwargs = {'video_id': video_id}), result.message))
        
        video =Video.objects.get(id=video_id)
        
        if not star_id:
            try:
                VideoStar.objects.create(video=video, identity=identity, name=name)
            except:
                return redirect('{}?error={}'.format(reverse('dashboard_videosub', kwargs = {'video_id': video_id}), '创建失败'))
        
        else:
            try:
                videostar = VideoStar.objects.get(id=star_id)
                videostar.name = name
                videostar.identity = identity
                videostar.save()
            except:
                return redirect('{}?error={}'.format(reverse('dashboard_videosub', kwargs = {'video_id': video_id}), '修改失败'))
            
            
        return redirect(reverse('dashboard_videosub', kwargs = {'video_id': video_id}))

class StarDelet(View):
    def get(self, request, star_id, video_id):
        star = VideoStar.objects.get(id=star_id)
        star.delete()
        
        return redirect(reverse('dashboard_videosub', kwargs = {'video_id': video_id}))
    
class SubDelet(View):
    def get(self, request, sub_id, video_id):
        sub = VideoSub.objects.get(id=sub_id)
        sub.delete()
        
        return redirect(reverse('dashboard_videosub', kwargs = {'video_id': video_id}))
    
class VideoUpdate(View):
    TEMPLATE = 'dashboard/video/videoupdtae.html'

    @dashboard_auth
    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        error = request.GET.get('error','')
        data = {}
        data['video'] = video
        data['error'] = error
        
        return render_to_response(request, self.TEMPLATE, data)
    
class VideoStatusUpdate(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=video_id)
        video.status = not video.status
        video.save()
        
        return redirect(reverse('dashboard_externalvideo'))
