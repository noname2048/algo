const ListNode = function (val, next) {
  this.val = val === undefined ? null : val;
  this.next = next === undefined ? null : next;
};

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @returns {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  if (!list1) return list2;
  else if (!list2) return list1;
  else if (list1.val <= list2.val) {
    list1.next = mergeTwoLists(list1.next, list2);
    return list1;
  } else {
    list2.next = mergeTwoLists(list1, list2.next);
    return list2;
  }
};

let ans = mergeTwoLists(
  new ListNode(1, new ListNode(2, new ListNode(4))),
  new ListNode(1, new ListNode(3, new ListNode(4))),
);

while (ans) {
  console.log(ans.val);
  ans = ans.next;
}
