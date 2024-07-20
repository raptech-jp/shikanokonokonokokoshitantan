import random

# 遷移
transitions = {
    'し': ['か', 'た'],
    'か': ['の'],
    'の': ['こ'],
    'こ': ['の', 'こ', 'し'],
    'た': ['ん'],
    'ん': [' ', 'た'],
}

# 重み
weights = {
    'し': [0.5, 0.5],
    'こ': [0.5, 0.25, 0.25],
    'ん': [0.5, 0.5],
}

# 初期状態
state = 'し'
result = [state]

# 最大14文字の文字列を生成、空白が出たら終了
while len(result) < 14:
    next_state = random.choices(
        transitions[state],
        weights = weights.get(state, [1])
    )[0]
    result.append(next_state)
    state = next_state
    if state == ' ':
        break

# 結果出力
print(''.join(result))
