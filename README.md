# Already-done..? [끝난줄 알았지..?]

모두의 게임 with Python [With. 고연주, 이수빈]

#게임 구상 (아이디어)
- 지뢰찾기 업그레이드
- 지뢰찾기 + 폭탄해체 (+ 시간 제한) (+ 논리학 개념)
- 지뢰 발견 시 바로 게임 오버가 아닌 기회를 한 번 더 주자는 아이디어로 탄생
- 배경: 대학, 지뢰발견: 교수님의 과제 투척, 깃발: A+, 지뢰: 과제

#게임 목표
- 교수님이 내주신 모두 과제를 피하거나 과제의 내용을 맞춰 9x9 보드판을 채워나가기

#게임 규칙
1. 기존의 지뢰찾기 규칙과 동일하게 무작위로 칸 하나를 클릭한다. 
2. 숫자일 경우, 해당 칸의 숫자만 공개, 공백일 경우, 공백을 둘려싼 모든 숫자를 공개, 과제일 경우, 폭탄 해체 게임으로 전환된다. 
3. (과제 클릭 X) 숫자는 주위 8칸 안에 있는 과제의 수를 의미한다. 과제가 있다고 예상되는 곳에 A+를 투척한다.
4. 1.~3. 과정을 반복하여 모든 과제의 위치에 A+를 두면 게임을 승리한다.
5. (과제 클릭 O) 교수님이 과제를 내주셨다는 메시지가 뜨며 과제 해결 게임으로 화면이 전환된다.
6. 논리학 추론 문제를 시간 내에 정답을 맞추면 다시 지뢰찾기 게임 화면으로 돌아간다. 
7. 만약, 시간 초과 되거나 정답을 맞추지 못하면 게임이 종료된다.

#참고자료 (Thanks to)
https://minesweeper.online/ko/
https://play.google.com/store/apps/details?id=com.panu&hl=ko&gl=US
https://www.flaticon.com/
https://www.thepythoncode.com/article/make-a-button-using-pygame-in-python?ref=morioh.com&utm_source=morioh.com
개인 프로젝트 01 : pygame으로 간단한 게임 만들기 (tistory.com)
Pygame_project : 6. 조건 설정 : 네이버 블로그 (naver.com)
[알고리즘/자바스크립트] 지뢰찾기 알고리즘 (Minesweeper Algorithm) :: Code Playground (tistory.com)
Python으로 지뢰찾기 만들기 (tistory.com)
[python] 지뢰찾기 만들기 (velog.io)
