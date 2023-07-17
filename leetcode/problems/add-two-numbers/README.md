linked list 에는 dubmmy head 기법이 속도를 줄이는데 있어 유용하게 쓰인다.
while 문 안에서 조건문을 늘리는 것보다
while 문 바깥에서 한번더 처리를 하는게 while 문내의 expression 을 줄이기 때문으로 사료된다.

v1 85ms(34.33%) -> v2 35ms(84.76%)
