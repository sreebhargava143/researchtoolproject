function addCard(data, id) {
    hash = "hashedId" + id
    feeds = document.getElementById("feed-card")

    newCard = document.getElementById("card").cloneNode(true);
    feeds.appendChild(newCard)

    newCard = document.getElementById("card")
    newCard.classList.remove("d-none");
    newCard.id = "card" + hash

    newTitle = document.getElementById("title")
    newTitle.innerHTML = data.title
    newTitle.id = "title" + hash

    newAuthor = document.getElementById("author")
    newAuthor.innerHTML = (data.author || 'Anonymous')
    newAuthor.id = "author" + hash

    newContentButton = document.getElementById("content-button")
    newContentButton.id = "content-button" + hash
    newContentButton.href = "#content" + hash
    newContentButton.setAttribute("aria-controls", "content" + hash)

    newContent = document.getElementById("content")
    newContent.id = "content" + hash

    newContentBody = document.getElementById("content-body")
    newContentBody.id = "content-body" + hash
    newContentBody.innerHTML = data.content

    newImage = document.getElementById("image")
    newImage.id = "image" + hash
    newImage.src = data.urlToImage

    newDescription = document.getElementById("description")
    newDescription.id = "description" + hash
    newDescription.innerHTML = data.description

    newBibliography = document.getElementById("bibliography")
    newBibliography.id = "bibliography" + hash
    newBibliography.href = data.url

    newDatePosted = document.getElementById("date-posted")
    newDatePosted.id = "date-posted" + hash
    dataTime = data.publishedAt.split("T")
    newDatePosted.innerHTML = dataTime[0]

    newTimePosted = document.getElementById("time-posted")
    newTimePosted.id = "time-posted" + hash
    newTimePosted.innerHTML = dataTime[1].split("Z")[0]

    newPublishedAt = document.getElementById("published-at")
    newPublishedAt.id = "published-at" + hash
    newPublishedAt.value = data.publishedAt

    if(data.id){
        newBookmarkId = document.getElementById("bookmark-id")
        newBookmarkId.id = "bookmark-id"+hash
        newBookmarkId.value = data.id

        newBookmark = document.getElementById("bookmark")
        newBookmark.id = hash
        newBookmark.addEventListener("click", deleteBookmark);
        newBookmark.innerHTML = "Delete"
        newBookmark.classList.remove("btn-info");
        newBookmark.classList.add("btn-danger")
    }
    else {
        newBookmark = document.getElementById("bookmark")
        newBookmark.id = hash
        newBookmark.addEventListener("click", addToBookmark);
    }

}

function deleteBookmark(e) {
    e = e || window.event;
    e = e.target || e.srcElement;
    var hash = ""
    if (e.nodeName === 'BUTTON') {
        hash = e.id
        feedCard = document.getElementById("card" + e.id)
        csrf = document.getElementById("csrf").value 
        bookmarkId = document.getElementById("bookmark-id" + e.id).value
        fetch("http://localhost:8000/bookmarks/"+bookmarkId, 
        {
            method: "DELETE",
            headers:{
                'X-CSRFToken': csrf,
                'content-type': 'application/json'
            }
        }
        );
        feedCard.parentNode.removeChild(feedCard);
    }

}
function addToBookmark(e) {
    e = e || window.event;
    e = e.target || e.srcElement;
    var hash = ""
    if (e.nodeName === 'BUTTON') {
        hash = e.id
        feedCard = document.getElementById("card" + e.id)

        cardData = {
            user_id : parseInt(document.getElementById("user_id").value),
            title: document.getElementById("title" + e.id).innerText,
            author: document.getElementById("author" + e.id).innerText,
            content: document.getElementById("content" + e.id).innerText,
            urlToImage: document.getElementById("image" + e.id).src,
            description: document.getElementById("description" + e.id).innerText,
            publishedAt: document.getElementById("published-at" + e.id).value,
            url: document.getElementById("bibliography" + e.id).href
        }
        cardData = JSON.stringify(cardData)
    }
    storeBookmark(cardData)
    feedCard.parentNode.removeChild(feedCard);

}

function postBookmarks(data){
    for (feed in data.results) {

    addCard(data.results[feed], feed)
    }
}

function storeBookmark(cardData){
    csrf = document.getElementById("csrf").value 
        fetch("http://localhost:8000/bookmarks/", 
        {
            method: "POST",
            body: cardData, 
            headers:{
                'X-CSRFToken': csrf,
                'content-type': 'application/json'
            }
        })
        .then(res=>res.json());
}

function postFeeds(data){
    for (feed in data.articles) {
        addCard(data.articles[feed], feed)
    }
}

function getFeeds() {
    var url = 'https://newsapi.org/v2/top-headlines?' +
        'country=in&'+
        'apiKey=fb1c2caa84c441d890f12f20499c4604';
    var req = new Request(url);
    fetch(req)
        .then(response => response.json())
        .then(data => {
            postFeeds(data)
        });
}

function explore_bookmarks() {
    user_id = document.getElementById("user_id").value,
    fetch("http://localhost:8000/bookmarks")
        .then(res => res.json())
        .then(data => {
            postBookmarks(data)
            }
        );
}

function search(query = "trending topics") {

    var url = 'https://newsapi.org/v2/everything?' +
        'q='+query+'&' +
        'from=2019-10-20&' +
        'sortBy=popularity&' +
        'laguage=en&' +
        'apiKey=fb1c2caa84c441d890f12f20499c4604';

    var req = new Request(url);

    fetch(req)
        .then(response => response.json())
        .then(data => {
            postFeeds(data)
        });
}
