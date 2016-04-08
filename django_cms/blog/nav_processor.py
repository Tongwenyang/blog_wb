#coding:utf-8
from .models import Column




def nav_column(request):
	'''
		让导航栏一直显示，不用每个views都传数据
	'''
	nav_display_columns = Column.objects.filter(nav_display=True)
	return {'nav_display_columns': nav_display_columns}