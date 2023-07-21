// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  const head = new ListNode(-1);
  let tail = head;

  // cmp
  while (list1 && list2) {
    if (list1.val < list2.val) {
      tail.next = new ListNode(list1.val);
      tail = tail.next;
      list1 = list1.next;
    } else {
      tail.next = new ListNode(list2.val);
      tail = tail.next;
      list2 = list2.next;
    }
  }
  // n cmp
  while (list1 !== null) {
    tail.next = new ListNode(list1.val);
    list1 = list1.next;
    tail = tail.next;
  }

  while (list2 !== null) {
    tail.next = new ListNode(list2.val);
    list2 = list2.next;
    tail = tail.next;
  }

  const ret = head.next;
  head.next = null;
  return ret;
};

let ans = mergeTwoLists(
  new ListNode(1, new ListNode(2, new ListNode(4))),
  new ListNode(1, new ListNode(3, new ListNode(4))),
);

while (ans) {
  console.log(ans.val);
  ans = ans.next;
}
