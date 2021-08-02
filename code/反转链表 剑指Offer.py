# 给定一个链表
# 输出反转后的链表
# 思路：第一个节点指向最后，后续每个节点指向前一个节点，注意当前节点与下一个节点的变量的转换。
#	    创建一个前置节点，用于最后的返回

class ListNode():
	#链表数据格式
	def __init__(self,x:int,left=None,right=None):
		self.val = x
		self.left = left
		self.right = right

		
#假设已经有了一个需要反转的链表 NodeX

		
def replaceNode(head):
	preHead = ListNode(0)
	preHead.next = head
	thisHead = head
	last = None
	while(thisHead):
		this = thisHead
		thisHead = this.next
		this.next = last
		last = this
	return preHead.next

