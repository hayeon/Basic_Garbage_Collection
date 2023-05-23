## Garbage Collection

![제목을-입력해주세요_-001](https://github.com/hayeon/Coin_Tracker/assets/81798537/8e446d4c-ebce-4243-a35e-5e187b8adb7e)

1. [가비지 콜렉션(Garbage Collection)의 개념](#가비지-콜렉션garbage-collection의-개념)

2. [가비지 콜렉션(Garbage Collection)의 종류](#가비지-콜렉션garbage-collection의-종류)
- [1. Tracing Garbage Collection(추적 기반 쓰레기 수집)](#1-tracing-garbage-collection추적-기반-쓰레기-수집)
- [2. Reference Counting based garbage collection(참조 횟수 카운팅 기반 쓰레기 수집)](#2-reference-counting-based-garbage-collection참조-횟수-카운팅-기반-쓰레기-수집)
3. [파이썬에서의 GC](#파이썬에서의-gc)

4. [예제코드](#예제코드)

<br/>
<br/>
<br/>

## 가비지 콜렉션(Garbage Collection)의 개념

> <b>가비지 콜렉션(Garbage Collection)</b>이란 메모리 관리 기법 중 하나,로 프로그램이 동적할당했던 메모리 영역 중 필요없게 된 영역을 해제하는 기능입니다.<p>
<b> 즉, 프로그램에서 더 이상 사용하지 않는 메모리를 자동으로 정리하는 것을 말합니다. 직역 그대로 '쓰레기 수집'이라고도 합니다. </b>

<br/>

## 가비지 콜렉션의 필요성 
> 예전의 프로그래밍 언어는 동적인 메모리 할당 기능이 없거나 프로그래머가 할당한 뒤, 수동 해제하는 방식이었습니다. 이로 인해 메모리 해제를 하지 않아 메모리 누수가 발생하거나, 해제했던 메모리를 다시 해제하는 등의 실수가 일어났습니다. 이는 프로그램의 수많은 취약점을 가져왔습니다. 이를 해결하기 위해 제시된 것이 "Garbage Collection (쓰레기 수집)"입니다. 프로그래머에게 직접적인 메모리 할당과 해제를 하게 하는 대신, 쓰레기 수집기에서 제공하는 할당과 해제를 사용하여 프로그램이 실행되며 쓸모가 없어진 메모리(쓰레기)를 수집합니다.
---
<br/>
<br/>


# 가비지 콜렉션(Garbage Collection)의 종류
## 1. Tracing Garbage Collection(추적 기반 쓰레기 수집)

> 프로그램 시, 특정 타이밍에 할당된 모든 메모리를 조사하여 현재 접근 가능한지 불가능한지 분류한 뒤, 접근 불가능한 메모리를 Garbage로 간주하여 해제시키는 방식입니다. 

 (1)  mark-and-sweep(표시하고 쓸기 기법) <P>
 ![sweep](https://github.com/hayeon/Coin_Tracker/assets/81798537/331ffb56-b01f-4438-9cd3-c6e2bf7c0408)
- 가장 단순한 방식으로 프로그램 실행 중 적당한 타이밍에 GC를 실행시켜 접근 가능한 메모리에 마킹(mark)을 한 후, 마킹이 안 된 메모리는 전부 할당 해제(sweep)하는 방식입니다.<p>
- 부가적인 작업 없이 접근 가능/불가능을 완벽하게 분류& 해제하는 것이 가능하지만, 
중간에 메모리가 변경되면 마킹을 다시 해야하기 때문에
프로그램을 통째로 정지(stop-the-world)시켜야 합니다. <p>
- 이 때문에 프로그램 실행 도중, 멈추는 시간이 발생합니다.

 (2) Incremental Garbage Collection(점진적 쓰레기 수집)<P>
 - 마킹과 해제를 한번에 하지 않고 여러 번에 걸쳐서 조금 씩 수행하는 방식입니다. 
 - Tracing Garbage Collection에 비해 수집과 해제라는 한 사이클에 걸리는 시간은 더 오래 걸리지만, GC를 수행할 때 프로그램 정지 시간을 줄일 수 있습니다.

### * tri-color marking(삼색기법) <P>
![tri-color](https://github.com/hayeon/Coin_Tracker/assets/81798537/458b5d9c-4368-4ebf-87ad-f660fd37111d)
1. 더 이상 접근 불가능한 메모리를 흰색으로 마킹 <p>
2. 접근 가능하지만, 해당 메모리에서 참조하는 메모리의 마킹을 하지 않은 경우 회색<p>
3. 접근 가능하며 해당 메모리가 참조하는 메모리의 마킹도 끝났으면 검은색<p>
4. 처음에 root를 조사하다, 흰색 메모리를 발견하면 회색으로 마킹합니다. <P>
5. root를 모두 마킹했으면 회색으로 마킹된 메모리를 조사하여 해당 메모리가 참조하는 모든 메모리까지 회색으로 마킹합니다.<P>
6. 이 작업이 끝나면 처음 회색이었던 메모리를 검은색으로 바꿉니다. <P>
7. 회색으로 마킹된 메모리가 존재하지 않으면 모두 흰색이나 검은색일 것이고, 접근 가능 여부가 결정됩니다.<P>
<br/>

<em>임의로 GC를 중단하여도, 다음번에 회색인 메모리부터 다시 조사하여 여러 번에 걸쳐서 GC를 수행할 수 있습니다. 
 <P> 또한 메모리가 고갈되었을 때 쓰레기 수집을 실행하는 것이 아니라 주기적으로 수집하는 것도 가능합니다. </em>
<br/>
<br/>

---

## 2. Reference Counting based garbage collection(참조 횟수 카운팅 기반 쓰레기 수집)

> * 다른 메모리가 얼마나 많이 참조하는지 횟수를 세어 접근 가능과 불가능을 나누는 방식입니다.
> * 한 메모리에서 다른 메모리를 참조하면 그 다른 메모리의 참조 횟수에 +1, 참조를 중단하면 참조 횟수에 -1을 수행합니다. 
> * 만약 -1을 수행할 경우 참조 횟수가 0이 되면 해당 메모리에 아무도 접근을 못 하는 것이므로 해당 메모리를 해제하게 됩니다.<p>
> * <b> CPython에서 이 방식을 사용하고 있습니다. </b>



### <b>장점</b>

객체가 접근 불가능해지는 즉시 소멸되어 프로그래머가 객체의 해제 시점을 어느 정도 예측할 수 있습니다.


### <b>단점</b>
<b>강한 참조 사이클(Strong Reference Cycle)로 인한 메모리 누수</b>: 2개 이상의 객체가 서로를 가리키고 있을 경우, 참조 횟수가 0이 되지 않게 됩니다. 이를 <b>순환참조</b>라고도 하며, <b>메모리 누수</b>가 발생합니다.
-  (1) A가 B를 가리키고, B에서 A를 가리키면 모두 참조 횟수는 1이다. 
- (2) A, B에 접근할 수 없지만 둘 다 참조 횟수가 0이 아니라서 해제할 수가 없으며, 그대로 메모리 누수가 발생한다. 

<p> CPython은 이를 해결하기 위해 순환 참조를 감지하는 추적 기법 알고리즘(Tracing GC)을 사용합니다. <p> 또한 자료구조에서 약한 참조(Weak Reference: 참조 횟수를 증가시키지 않는 포인터)를 사용하여 이 문제를 해결할 수 있습니다.

<br/>

---

# 파이썬에서의 GC
> 파이썬에선 GC 모듈을 제공합니다. 

|모듈|내용|
|------|---|
|gc.enable()|GC 활성화|
|gc.disable()|GC 비활성화|
|gc.isenabled()|활성화되어 있는지 여부를 반환. 활성화되어 있으면 True, 비활성화되어 있으면 False|
|gc.collect([generation])|GC 수동 수행|
|gc.set_debug(flags)|GC 버깅 플래그를 설정합니다. 디버깅 정보가 sys.stderr에 기록됩니다.|
|gc.get_count()|현재 수거 횟수를 (count0, count1, count2)의 튜플로 반환합니다.|
|gc.get_threshold()|현재 세대별 GC 임계값을 (threshold0, threshold1, threshold2)의 튜플로 반환|
|gc.get_objects()|현재 추적되고 있는 모든 객체의 리스트를 반환|


<br/>

# 예제코드

---

## gc모듈 사용하기

```python
import gc

class AClass:
    def __init__(self, name):
        self.name = name
        print(f'{self.name}'이 생성되었습니다.)

    def __del__(self):
        print(f' {self.name}'이 제거되었습니다.)

# GC를 수행하기 위해 임의의 객체 생성
def trigger_garbage_collection():
    # 10,000개의 AClass 객체 생성
    objects = [AClass(str(i)) for i in range(10000)]
    print('GC가 수행됩니다.')
    gc.collect() # gc을 강제로 수행합니다.
    print('GC가 종료되었습니다.')

trigger_garbage_collection()  # gc 트리거 함수를 호출합니다.
```
> AClass 객체가 생성될 때마다 생성 메시지가 출력되고, 객체 소멸 시 소멸 메시지가 출력됩니다.<P>
trigger_garbage_collection 함수는 10,000개의 AClass 객체를 생성한 다음, GC를 수동으로 트리거합니다. <p> 
gc.collect()를 호출하여 GC를 강제로 실행합니다. 그 후에 "GC가 종료되었습니다." 메시지가 출력됩니다.

<br/>
<br/>

---

## 예제코드- 강한 참조 사이클로 인한 Memory Leak 발생

```python
import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 노드를 생성하고 연결 리스트를 형성
def create_linked_list():
    head = Node(1)
    current = head
    for i in range(2, 100):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    # 연결 리스트의 끝을 처음 노드로 연결하여 사이클을 형성
    current.next = head
    return head

def main():
    linked_list = create_linked_list()
    # 연결 리스트를 출력합니다. 
    current = linked_list
    while current is not None:
        print(current.value)
        current = current.next

    # GC를 수동으로 호출하여 메모리 정리를 시도합니다.
    gc.collect()


if __name__ == '__main__':
    main()

```
 
### 실행결과 
 ![memoryleak](https://github.com/hayeon/Coin_Tracker/assets/81798537/ac660767-1c75-4a0d-aa63-aeecafe2059b)

 
>순환 사이클로 인해 연결 리스트에 대한 참조가 남아있으므로 메모리 누수가 발생합니다. <p> GC 모듈은 순환참조로 인한 메모리 누수를 해결할 수 없습니다. 따라서 프로그래머는 참조 사이클을 발생시키지 않도록 주의해야합니다. 

<br/>
<br/>

---
## 예제코드- 참조사이클이 없는 예제 코드

```python
import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 노드를 생성하고 연결 리스트를 형성합니다.
def create_linked_list():
    head = Node(1)
    current = head
    for i in range(2, 100):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    # 마지막 노드의 next 참조를 None으로 설정하여 사이클을 방지합니다.
    current.next = None
    return head

def main():
    linked_list = create_linked_list()
    # 연결 리스트를 출력합니다.
    current = linked_list
    while current is not None:
        print(current.value)
        current = current.next

    # GC를 수동으로 호출하여 메모리 정리를 시도합니다.
    gc.collect()

if __name__ == '__main__':
    main()


```
 ### 실행결과 
 <img width="495" alt="image" src="https://github.com/hayeon/Coin_Tracker/assets/81798537/cb08cb20-79c1-4b58-afb5-9500861ea396">
 
 <br/>

>create_linked_list() 함수의 마지막에서 마지막 노드의 next 참조를 None으로 설정하여 사이클을 방지합니다. <p> 이를 통해 모든 노드가 GC의 대상이 되어 메모리 누수가 발생하지 않습니다. <P>
수정된 코드를 실행하면 1부터 99까지의 숫자가 한 번씩 출력되며, 메모리 누수가 발생하지 않고 메모리가 정리되는 것을 확인할 수 있습니다.

<br/>
<br/>
<br/>


---
참고자료<p>
[Tracing garbage collection](https://en.wikipedia.org/wiki/Tracing_garbage_collection)<p>
[Garbage Collector interface](https://docs.python.org/ko/3.7/library/gc.html)
