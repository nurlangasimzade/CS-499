# CS 300 Project One: Runtime and Memory Analysis

This document contains the finalized pseudocode for the ABCU Computer Science advising program using three data structures: vector, hash table, and binary search tree (BST).

## Pseudocode Summary
- Vector: Simple order-preserving structure; O(n) search.
- Hash Table: O(1) average insert/search; requires sorting for ordered output.
- Binary Search Tree: Maintains order with O(log n) search/insert if balanced.

## Runtime Analysis
Vector: O(n + p) total cost for loading data.
Hash Table: O(n) for loading, O(1) average for search, plus sorting cost for ordered output.
BST: O(n log n) typical with balanced tree.

## Recommendation
Hash table recommended for best average-case performance on frequent lookups, with sorting applied when needed for ordered output.
