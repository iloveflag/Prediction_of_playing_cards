#coding=utf-8
import random
def b_should_choose(list1,list2,rand_before):
	cnt=0
	if len(list1)==1:
		for i in range(len(list2)):
			if list2[i]<list1[0]:
				cnt=cnt+1
		if cnt>1:
			print 'a win'
		else:
			print 'b win'
		begin_game()
		
	#如果a里面只剩一张牌，且比b里面大的牌超过1张，a win，
	#因为正常人看到对方只有一张牌，肯定是从大往小出
	can_list2=[]
	for j in range(len(list2)):
		if(list2[j]>rand_before):
			can_list2.append(list2[j])
	#b可以出的牌  
	put_choose=random.randint(0,1)
	#b决定要不要出
	if can_list2==[]:
		put_choose=0
	#没有比他大的牌了
	if(put_choose):
	#b出牌
		rand_b=can_list2[random.randint(0,len(can_list2)-1)]
		list2.remove(rand_b)
		who_next_choose=0
		rand_before=rand_b
		# print 'b出牌:'+str(rand_before)		
	#下一个a出牌
		return(list1,list2,who_next_choose,rand_before)
	else:
		# print 'b不出'
		rand_a_again=list1[random.randint(0,len(list1)-1)] 
		rand_before=rand_a_again
		# print 'a再出一张'+str(rand_before)
		list1.remove(rand_a_again)			
		who_next_choose=1
	#轮到b出了
		return(list1,list2,who_next_choose,rand_before)
def a_should_choose(list1,list2,rand_before):
	cnt=0
	if len(list2)==1:
		for i in range(len(list1)):
			if list1[i]<list2[0]:
				cnt=cnt+1
		if cnt>1:
			print 'b win'
		else:
			print 'a win'
		begin_game()
	can_list1=[]
	for j in range(len(list1)):
		if(list1[j]>rand_before):
			can_list1.append(list1[j])
	#a可以出的牌  
	#print can_list1
	put_choose=random.randint(0,1)
	if can_list1==[]:
		put_choose=0
	#a决定要不要出
	if(put_choose):
	#a出牌
		rand_a=can_list1[random.randint(0,len(can_list1)-1)]
		list1.remove(rand_a)
		who_next_choose=1
		rand_before=rand_a
		# print 'a出牌:'+str(rand_before)
	#下一个b出牌
		return(list1,list2,who_next_choose,rand_before)
	else:
		# print 'a不出'		
		rand_b_again=list2[random.randint(0,len(list2)-1)] 
		list2.remove(rand_b_again)
		rand_before=rand_b_again
		# print 'b再出一张'+str(rand_before)
		who_next_choose=0
	#轮到a出了
		return(list1,list2,who_next_choose,rand_before)
def begin_game():
	global run_cnt
	run_cnt=run_cnt+1
	if run_cnt>100:
		exit()
	#测试次数
	list1=[17,12,7,7,7,4]
	list2=[16,13,13,13,11,9]
	rand_before=3
	(list1,list2,who_next_choose,rand_before)=b_should_choose(list1,list2,3)
	while(1):
		# print 'a剩下：'+str(list1)
		# print 'b剩下:'+str(list2)
		if(who_next_choose): 
			(list1,list2,who_next_choose,rand_before)=b_should_choose(list1,list2,rand_before)
		else:
			(list1,list2,who_next_choose,rand_before)=a_should_choose(list1,list2,rand_before)
run_cnt=0
begin_game()






	
	
