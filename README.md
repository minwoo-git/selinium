## 실행
- chrome 및 chrome driver는 설정되어 있다고 가정
- (`windows_chrome` 폴더에서)
  - 브라우저 화면 보기: `python rubuto_next.py"  
  - 브라우저 화면 없이: `python rubuto_next_headless.py`

## Problem & Solution
### Next 버튼 클릭 불가 문제

- 문제: next 버튼 클릭 시, `selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted` 발생
- 원인: (Windows & Chrome 환경에서) next 버튼을 menu-decoder가 가림
- 해결: next 버튼 클릭 전, menu-decoder 삭제
  https://github.com/minwoo-git/selinium/blob/c1b8df698c2e52ebc12808c97a3f5abd5d99ebda/windows_chrome/rubato_next.py#L17-L18
