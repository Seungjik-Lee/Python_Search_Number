file= open("number.txt","a")
f= open("number.txt","r")
phone_number=dict()

name_store=[]
number_store=[]
for line in f:
    line = line.strip()
    line = line.split()
    phone_number[line[0]]=line[1]
    


def add():
    store=input("추가할 사람 혹은 가게이름을 입력하세요: ")

    if store in phone_number:
        print()        
        print("이미 해당 전화번호가 존재합니다. 전화번호를 검색해보세요")
        print()
    else:
        number=input("전화번호를 입력하세요.(예)0xx-123-4567: ")
        file.write(store+'\t')
        file.write(number+'\n')
        phone_number[store]=number
        print()
        print("전화번호를 추가했습니다.")
        print("이름: ",store)
        print("전화번호: ",number)
        print()
        for i in phone_number:
            print("('" + i + "', '" + phone_number[i] + "')")

def search():
    storecheck=input("사람 혹은 가게이름을 입력하세요:")

    if storecheck not in phone_number:
        print()
        print("죄송합니다. 해당 전화번호는 없습니다.")
        print()
        for i in phone_number:
            print("('" + i + "', '" + phone_number[i] + "')")
    else:
        print()
        print("문의하신 전화번호는 [",phone_number[storecheck],"]입니다.")
        print()
        for i in phone_number:
            print("('" + i + "', '" + phone_number[i] + "')")

while True:
    print("1. 전화번호 검색") 
    print("2. 전화번호 추가")
    print("3. 종료")
    menu=int(input("메뉴를 선택하세요: "))
    if menu==1:
        search()
    elif menu==2:
        add()
    elif menu==3:
        print("프로그램을 종료합니다.")
        break
    else:
        print("1~3 번 중 입력하세요.")
        continue

file.close()
f.close()
