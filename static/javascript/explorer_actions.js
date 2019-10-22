
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

    if (data.id) {
        newBookmarkId = document.getElementById("bookmark-id")
        newBookmarkId.id = "bookmark-id" + hash
        newBookmarkId.value = data.id

        newBookmark = document.getElementById("bookmark")
        newBookmark.id = hash
        newBookmark.addEventListener("click", deleteBookmark);
        newBookmark.innerHTML = "Delete"
        newBookmark.classList.remove("btn-info");
        newBookmark.classList.add("btn-danger")
    } else {
        newBookmark = document.getElementById("bookmark")
        newBookmark.id = hash
        newBookmark.addEventListener("click", promptName);
    }
    return newCard
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
        fetch("http://localhost:8000/bookmarks/" + bookmarkId, {
            method: "DELETE",
            mode: "no-cors",
            headers: {
                'X-CSRFToken': csrf,
                'content-type': 'application/json'
            }
        });
        feedCard.parentNode.removeChild(feedCard);
    }
}
function closePromptName(){
    document.getElementById("bookmark-name").value = ""
    document.getElementById("prompt-name").style.display = 'none';
}
function promptName(e) {
    e = e || window.event;
    e = e.target || e.srcElement;
    popUp = document.getElementById("prompt-name").style.display = 'block';
    popUp.focus="focus";
    document.getElementById("hash").value = e.id
}

function checkBookmarkName() {
    name = document.getElementById('bookmark-name').value
    fetch("http://localhost:8000/bookmarks/names/"+name+"/",{mode: "no-cors"})
        .then(res => res.json())
        .then(data => {
            if (data.response) {
                alert("Name already exists provide other name!");
                document.getElementById('bookmark-name').focus();
            } else {
                addToBookmark()
                document.getElementById("prompt-name").style.display = 'none';
            }
        });
}

function addToBookmark() {
    hash = document.getElementById("hash").value
    feedCard = document.getElementById("card" + hash)
    cardData = {
        bookmark_name: document.getElementById("bookmark-name").value,
        user_id: parseInt(document.getElementById("user_id").value),
        title: document.getElementById("title" + hash).innerText,
        author: document.getElementById("author" + hash).innerText,
        content: document.getElementById("content" + hash).innerText,
        urlToImage: document.getElementById("image" + hash).src,
        description: document.getElementById("description" + hash).innerText,
        publishedAt: document.getElementById("published-at" + hash).value,
        url: document.getElementById("bibliography" + hash).href
    }
    document.getElementById("bookmark-name").value = ""
    cardData = JSON.stringify(cardData)
    storeBookmark(cardData)
    feedCard.parentNode.removeChild(feedCard);

}

function postBookmarks(data) {
    for (feed in data.results) {

        addCard(data.results[feed], feed)
    }
}

function storeBookmark(cardData) {
    csrf = document.getElementById("csrf").value
    fetch("http://localhost:8000/bookmarks/", {
            mode:"no-cors",
            method: "POST",
            body: cardData,
            headers: {
                'X-CSRFToken': csrf,
                'content-type': 'application/json'
            }
        })
        .then(res => res.json());
}

function postFeeds(data) {
    for (feed in data.articles) {
        addCard(data.articles[feed], feed)
    }
}

function getFeeds() {
    var url = 'https://newsapi.org/v2/top-headlines?' +
        'country=in&' +
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
        fetch("http://localhost:8000/bookmarks/", {mode:"no-cors"})
        .then(res => res.json())
        .then(data => {
            postBookmarks(data)
        });
}

function search(query = "trending topics") {

    var url = 'https://newsapi.org/v2/everything?' +
        'q=' + query + '&' +
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
