# 141_linked_list_cycle

実施日: 2026-05-24

## step1

Good
- 数年前に過去に解いたことがあり2パターンでの実装ができた

Bad
- submissionが1発で通らなかった。nodeの比較ではなくvalの比較をしていた。

## step2
三項演算子の実装はぱっと見シンプルに書けているが、ロジックが追いにくくなっているかもしれない

Good
- 特になし

Bad
- 特になし

Geminiによる英語の添削

```
# Memo
# Strategy 1: Traverse all nodes from the head and store them to track visited nodes.
# If a node is revisited, the list contains a cycle.
# This approach is easy to implement but requires O(n) space complexity.

# Strategy 2: Use two pointers moving at different speeds. The first pointer moves 1 node 
# per step, while the second pointer moves 2 nodes per step.
# This approach is a bit tricky but achieves O(1) space complexity.

# Example: A -> B -> C -> D -> A
# First Pointer:  A -> B -> C -> D
# Second Pointer: B -> D -> B -> D
```