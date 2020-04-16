# Css Animation
# 1. CSS의 탄생 배경 및 정의

    웹사이트는 HTML언어로 이루어져있습니다. HTML언어는 ```<head></head>```등과 같은 태그로 이루어지고 
    이 태그 사이의 코드는 웹사이트의 많은 정보를 담고 있습니다. 
    
    특히, 웹사이트의 디자인과 관련된 정보는 상당히 많은데 이 디자인과 관련된 코드만 따로 작성할 수 있도록 
    CSS라는 새로운 언어를 만들었습니다.

# 2. CSS문법

 ### **1. CSS를 적용하는 방법**

HTML 문서에 CSS 스타일을 적용할 때에는 다음과 같이 세 가지 방법을 사용할 수 있습니다.
 

1.) 인라인 스타일(Inline style)

2.) 내부 스타일 시트(Internal style sheet)

3.) 외부 스타일 시트(External style sheet)

    
        외부 스타일 시트를 이용하는 방법은 웹 사이트 전체의 스타일을 하나의 파일에서 변경할 수 있도록 해줍니다.
    
        외부에 작성된 이러한 스타일 시트 파일은 .css 확장자를 사용하여 저장됩니다.
    
        스타일을 적용할 웹 페이지(html코드를 작성한 파일)의 <head>태그에 <link>태그를 사용하여 
        외부 스타일 시트를 포함해야만 스타일이 적용됩니다.
    
### **2. CSS의 문법**

        CSS는 선택자(selector)와 선언부(declaratives)로 구성됩니다.
        
        
        선택자는 CSS를 적용하고자(디자인 효과를 주고 싶은) 하는 HTML 요소(element)를 가리킵니다.
        
        
        선언부는 중괄호{ }를 사용하여 전체를 둘러쌉니다.
        
            CSS는 특정한 기능을 하는들이 미리 정의되어 있으며, 이를 활용하여 태그의 스타일을 정의할 수 있습니다.
        
            각 선언은 CSS 속성명(property)과 속성값(value)을 가지며, 그 둘은 콜론(:)으로 연결됩니다.
        
            CSS 선언(declaration)은 마지막에 세미콜론(;)으로 끝마칩니다.
        
```html
body{                                |선택자               #body에 효과를 적용한다.
	background-color: orange;    |선언부{속성 : 값};    #배경색은 주황색으로 적용한다.
        width:256px;                 |                     #너비는 256px로 적용한다.
	height:300px;                |                     #높이는 300px로 적용한다.
}                                    
```

# 3. 실습
이번 시간에는 외부 스타일 시트를 이용하여 css를 적용해봅시다.

개발환경(노트패드/파이참)에서 html코드와 css코드를 작성할 수 있도록 준비합니다.

우선 html코드부터 작성합니다.

이 때 href는 연결할 주소를 지정 하는 태그로서 .**css파일의 이름과 같아야 합니다.**
```html
<html lang="en">
<head>
    <title>character_walking</title>
	<link rel="stylesheet" href="CssAnimation.css">
</head>
```
body 태그를 작성한다.
```html

<body>
        <div id="runner"></div>
		<div id="road"></div>
</body>
</html>

```

이제 css코드를 작성한다.

우선, 구글에서 spritesheet을 검색한다.

이미지를 우클릭해서 ***이미지 주소를 복사***한 뒤 back ground속성 뒤 url에 붙여준다.

이미지를 다운받고, 다운받은 이미지를 우클릭-->자세히-->이미지의 너비와 높이를 확인한다.

width속성 뒤의 값으로 다운받은 이미지의 너비를 runner의 수만큼 나눠서 넣어준다.

height속성 뒤의 값으로 복사를 넣어준다.

```css
body{
	background-color: orange;
}

#road{
	border-bottom: 7px dotted black;	/*solid, dotted, rigid*/
}

#runner{
	background:url("https://www.codeandweb.com/blog/2016/05/10/how-to-create-a-sprite-sheet/spritestrip.png");

	width:256px;
	height:256px;
	animation:walk 1s steps(6) infinite,
				forward 5s linear infinite;
}
```
나머지 속성과 값을 적어주면서 코드를 완성한다.

```css
@keyframes walk{
	0%{
		background-position: 0px;
	}
	100%{
		background-position: 3000px;
	}
}

@keyframes forward{
	0%{
		transform:translateX(-100px);
	}

	100%{
		transform:translateX(1200px);
	}
}
```
