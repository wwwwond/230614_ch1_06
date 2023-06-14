# 리스트 응용

## 리스트 조작하기

### 리스트에 요소 추가하기

'''
* append : 요소 하나를 추가 (맨 뒤에)
* extend : 리스트를 연결하여 확장
* insert : 특정한 인덱스에 요소를 추가
'''

### 기존 리스트에 요소 하나 추가하기

a = [10, 20, 30]
print(a)
# a = [10, 20, 30, 500] # 재할당 (다시 대입하지 않아도...)
a.append(500) # append : 리스트 맨 뒷자리에 새로운 원소(요소)를 추가
# ? : 없던 인덱스에는 값을 할당할 수 X -> append를 사용하게 되면 신규 인덱스를 생성 및 값 할당
# '리스트'라는 자료형, 타입, 클래스에 딸린 내장 기능 = 메소드.
print(a)

# b = []
b = list()
print(b)
b.append(10)
print(b)

### 리스트 안에 리스트 추가하기
l = [[0] * 5] * 5 # 행 -> 열
print(l, len(l))
l.append([1])
print(l, len(l))  # append 시에 길이는 무조건 1씩 증가

### 리스트 확장하기
a = ["사과"]
b = ["배"]
print(a + b)
a = ["사과"] * 3
print(a)
a.extend(b)  # append, extend -> 다시 할당/대입 과정?
# inplace -> 대체 -> 메소드를 실행하는 순간 굳이 재대입/재할당 -> 원래 변수에 영향을 미친다
print(a)
print(a + b)
print(a + b)
print(a + b)
print(a + b)
print(a) # a는 변하지 않는다! (연산자로 하면) *, + 똑같은데...
# append, extend? -> 원본에 영향을 미친다 (할당연산자 없이 쓰는 애들)
# extend  => + 가 아니라 += 의 역할을 한다
# extend는 전달받은 리스트의 원소를 하나씩 반복하면서 append라고 보시면 됨.
l = [1, 2 ,3]
l2 = [4, 5, 6]

#1.
l3 = l + l2
print("#1", l3)

#2.
l3 = []
l3.extend(l)
l3.extend(l2)
print("#2", l3)

#3.
l3 = []
for v1 in l:
    l3.append(v1) # 2배씩으로 만들어서 더해야한다
for v2 in l2:
    l3.append(v2)
print("#3", l3)

#3-1.
l3 = []
for v1 in l:
    # break? continue?
    l3.append(v1 * 2) # 2배씩으로 만들어서 더해야한다
for v2 in l2:
    l3.append(v2 * 2)
print("#3", l3)

### 리스트의 특정 인덱스에 요소 추가하기
# 리스트객체.insert(인덱스, 요소)는 리스트의 특정 인덱스에 요소 하나를 추가합니다.
a = list(range(10, 40, 10))
print(a)  # [10, 20, 30]
# a.insert(2, 15)  # 인덱스 2번째
a.insert(1, 15)  # 순서상 2번째 자리
print(a)
'''
* insert(0, 요소): 리스트의 맨 처음에 요소를 추가
* insert(len(리스트), 요소): 리스트 끝에 요소를 추가
'''
a.insert(0, 5)  # 파이썬 상 속도를 많이 잡아먹음 -> stack, queue, deque. (자료구조)
# index 바탕으로 어느 지점에 값을 넣어줘야하나 '찾는 로직' => 느린 메소드.
a.insert(len(a), 100)  # 굳이 할 필요가 없다
# a.append(100)
print(a)


### 리스트에서 요소 삭제하기
print("삭제 전", a)
del a[0]
print("삭제 후", a)
store = [10000, 2000, 5162]
# 가장 마지막 결제한 금액을 확인해서 print하고, 해당 값을 (리스트에서) 삭제
print(store)
print(store[-1])
del store[-1]
print(store)

# 리스트에서 특정 인덱스 값을 찾아서 삭제 -> 반환

store = [10000, 2000, 5162]
# 가장 마지막 결제한 금액을 확인해서 print하고, 해당 값을 (리스트에서) 삭제
print(store)
# print(store[-1])
# del store[-1]
# pop()은 리스트의 마지막 요소를 삭제한 뒤 삭제한 요소를 반환
p = store.pop() # pop(-1), pop(len(..)-1)
print(p)
print(store)

store = [10000, 2000, 5162]
print(store)
p = store.pop(0)  # 인덱스 -> 인덱스 번째의 값을 반환하고, 해당 값을 리스트에서 삭제
# 리스트객체.pop(인덱스) : 해당 인덱스의 값을 꺼내옴. (인덱스가 없으면 -1로 default)
print(p)
print(store)

# pop: 마지막 요소 또는 특정 인덱스의 요소를 삭제

# 리스트에서 특정 값을 찾아서 삭제
cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '레드벨벳 쿠키']
print(cookies)
# r = cookies.remove("치즈 쿠키")  # pop 처럼 삭제된 결과 X
# print(r)
cookies.remove("치즈 쿠키")  # pop 처럼 삭제된 결과 X
# 특정한 값을 찾는 기능.
print(cookies)
# 리스트.remove(값) -> 해당 값의 요소를 삭제

print(cookies.index("오레오 쿠키"))
# 리스트.index(값) -> 해당 값의 요소의 인덱스를 반환)
# idx = cookies.index("오레오 쿠키")
# del cookies[idx]
cookies.remove("오레오 쿠키")
print(cookies)

cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '마카다미아 쿠키', '레드벨벳 쿠키', '마카다미아 쿠키']
# index 혹은 remove 사용했을 때, 무엇을 검색 또는 삭제해줄까요?
print("cookies.index(\"마카다미아 쿠키\")", cookies.index("마카다미아 쿠키")) # 1개만 나옴
# 가장 먼저 발견되는 1개. (index 0부터해서...)

index = 0
value = "마카다미아 쿠키"
# for c in cookies:
# for i, c in enumerate(cookies):
for i in range(len(cookies)):
    # if c == value:
    if cookies[i] == value:
        # del(delete) ... -> remove
        break
    # index += 1
# print(index)
print(i)

print(cookies)
# print(cookies.index("초코파이")) # ValueError: '초코파이' is not in list
print("초코파이" in cookies)
# cookies.remove("초코파이") # list.remove(x): x not in list

store = ["마제소바", "토리동", "부타동"]
# while store:  # 리스트 -> False? -> 그 안에 요소가 없을 때...
while True:
    print(store)
    order = input("무엇을 주문하시겠습니까? : ")
    if order in store:
        store.remove(order)  # 요소를 계속 제거...
        print(order + "을(를) 드리겠습니다")
    else:
        print(order + "은(는) 현재 없는 메뉴입니다")
    if len(store) == 0: # if not store:
        break
print("장사 끝났습니다")

