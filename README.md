# Cafe_POS_System

![Image](https://github.com/user-attachments/assets/aec5899f-74db-4208-89d6-fdba170cc9b8)

"내가 만약... 카페 사장이라면..."

---

### **1. 회원 관리**  
- **회원 가입**  
  - **휴대폰 번호와 비밀번호**를 입력하여 회원 가입
  - 휴대폰 번호의 **유효성을 검증**
  - 비밀번호는 **안전하게 저장**될 수 있도록 보안 조치를 적용  

- **로그인 및 로그아웃**  
  - 회원 가입 후, **로그인**과 **로그아웃**
  - JWT토큰, (세션도 좋고요)

---

### **2. 상품 관리** *(로그인 후 이용 가능)*  
- **상품 속성 (필수)**  
  - 상품에는 다음과 같은 필수 속성이 포함되어야 합니다.  
    - 카테고리  
    - 가격  
    - 원가  
    - 이름  
    - 설명  
    - 바코드  
    - 유통기한  
    - 사이즈 (**small** 또는 **large**)  

- **상품 관련 기능**  
  1. **상품 등록**    
  2. **상품 수정**    
  3. **상품 삭제**    
  4. **상품 목록 조회**  
     - **커서 기반 페이지네이션**을 적용하며, **한 페이지당 10개**의 상품을 표시
  5. **상품 상세 조회**  
  6. **상품 검색**  
     - 상품 이름을 기반으로 **검색 기능**을 제공합니다.  
     - **LIKE 검색**과 **초성 검색**을 지원해야 합니다.  
       - 예) **카페 라떼** → 검색 가능한 키워드: **카페, 라떼, ㅋㅍ, ㄹㄸ**  

---

### **3. 접근 제한**  
- 로그인하지 않은 사용자는 **상품 관련 API에 접근할 수 없습니다.**  

---

> P.s: 지속적 업그레이드 예정.

