#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

typedef struct listint_t {
    int data;
    struct listint_t *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number) {
    
    listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
    if (!new_node) {
        // Allocation failed
        return NULL;
   }


    new_node->data = number;
    new_node->next = NULL;


    if (*head == NULL || number < (*head)->data) {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    listint_t *current = *head;
    while (current->next != NULL && current->next->data < number) {
        current = current->next;
    }

    
    new_node->next = current->next;
    current->next = new_node;

    return new_node;
}


void print_list(listint_t *head) {
    while (head != NULL) {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}


int main() {
    listint_t *head = NULL;

    insert_node(&head, 3);
    insert_node(&head, 5);
    insert_node(&head, 7);
    insert_node(&head, 9);

    printf("Original List: ");
    print_list(head);

    insert_node(&head, 6);

    printf("Updated List: ");
    print_list(head);

    return 0;
}

