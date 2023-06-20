// script.js

// 가지고 있는 재료를 서버에 전송하여 요리 추천 결과를 받아옵니다.
function getRecipeRecommendation() {
  const ingredients = document.getElementById('ingredients').value;

  // AJAX 요청 보내기
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/recipes/recommendation/');
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.onload = function() {
    if (xhr.status === 200) {
      // 응답 데이터를 처리하여 추천된 요리를 화면에 표시합니다.
      const response = JSON.parse(xhr.responseText);
      displayRecommendations(response.recipes);
    } else {
      // 요청이 실패한 경우 에러 처리를 합니다.
      console.error('Request failed. Status:', xhr.status);
    }
  };
  xhr.send('ingredients=' + encodeURIComponent(ingredients));
}

// 추천된 요리를 화면에 표시합니다.
function displayRecommendations(recipes) {
  const resultsContainer = document.getElementById('results');
  resultsContainer.innerHTML = '';
  if (recipes.length === 0) {
    const noResults = document.createElement('p');
    noResults.textContent = '추천된 요리가 없습니다.';
    resultsContainer.appendChild(noResults);
  } else {
    const ul = document.createElement('ul');
    recipes.forEach(function(recipe) {
      const li = document.createElement('li');
      li.textContent = recipe.name;
      ul.appendChild(li);
    });
    resultsContainer.appendChild(ul);
  }
}

// 요리 추천 버튼 클릭 이벤트 핸들러 등록
const recommendButton = document.getElementById('recommend-button');
recommendButton.addEventListener('click', function(event) {
  event.preventDefault();
  getRecipeRecommendation();
});
