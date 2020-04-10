# Css Animation
#1. CSS의 탄생 배경 및 정의

    웹사이트는 HTML언어로 이루어져있다. HTML언어는 ```<head></head>```등과 같은 태그로 이루어지고 이 태그 사이의 코드는 웹사이트의 많은 정보를 담고 있다. 
    
    한편, 웹사이트의 디자인과 관련된 정보는 상당히 많은데 이 디자인과 관련된 코드만 따로 작성할 수 있도록 CSS라는 새로운 언어를 만들었다.

#2. 혁명적 변화
1) 어떤 property(속성)들이 있을까 = 어떤 효과들이 웹페이지를 design할 수 있을까 

2) 어떤 선택자들이 있을까 = 효과를 정확하게 선택 및 지정하기 위해

3. CSS에서의 속성
웹페이지에 CSS를 삽입하는 방법


#3.실습
개발환경(노트패드/파이참)에서 html코드와 css코드를 작성할 수 있도록 준비한다.

우선 html코드부터 작성한다.

이 때 href는 연결할 주소를 지정 하는 태그로서 .**css파일의 이름과 같게**해야 한다.
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
