# VSCode拡張機能の確認（実行ボタン）
a = 1
b = 5
print(a + b)

# インデントの自動挿入
x = ['aaa', 'bbb', 'ccc']
y = ['eee',
     'fff',
     'ggg']

# 関数のドキュメントを"""で自動作成
def func1(x: str, y: int) -> str:
  return f'{x}は{y}円です'

def func2(x: str, y: int) -> str:
  """商品の価格説明文

  Args:
      x (str): 商品名
      y (int): 価格

  Returns:
      str: 説明文
  """
  return f'{x}は{y}円です'
