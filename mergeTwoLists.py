/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    
    struct ListNode * c1 = l1;
    struct ListNode * c2 = l2;
    if (c1 == NULL){
        return l2;
    }
    else if(c2 == NULL){
        return l1;
    }
    
    struct ListNode * n1 = l1;
    struct ListNode * n2 = l2;
    struct ListNode * cur = NULL;
    struct ListNode * head = NULL;

    int val1 = c1->val;
    int val2 = c2->val;
    
    if(val1 > val2){
        head = c2;
        n2 = n2->next;
    }
    else{
        head = c1;
        n1 = n1->next;
    }
    cur = head;
    
    while(n1 != NULL && n2 != NULL){
        val1 = n1->val;
        val2 = n2->val;
        if(val1 > val2){
            cur->next = n2;
            cur = n2;
            n2 = n2->next;
        }
        else{
            cur->next = n1;
            cur = n1;
            n1 = n1->next;
        }
    }
    
    if(n1 != NULL){
        cur->next = n1;
    }
    else{
        cur->next = n2;
    }
    
    return head;  
}