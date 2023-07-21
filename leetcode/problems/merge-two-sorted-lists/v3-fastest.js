const ListNode = function (val, next) {
  this.val = val === undefined ? -1 : val;
  this.next = next === undefined ? null : next;
};

var mergeTwoLists = function (list1, list2) {
  head = { val: -1, next: null };
  tail = head;

  while (list1 && list2) {
    if (list1.val <= list2.val) {
      tail.next = list1;
      list1 = list1.next;
    } else {
      tail.next = list2;
      list2 = list2.next;
    }
    tail = tail.next;
  }

  tail.next = list1 || list2;
  return head.next;
};

let ans = mergeTwoLists(
  new ListNode(1, new ListNode(2, new ListNode(4))),
  new ListNode(1, new ListNode(3, new ListNode(4))),
);

while (ans) {
  console.log(ans.val);
  ans = ans.next;
}
