function addCard(data, id) {

    hash = "hashedId" + id
    feeds = document.getElementById("feed-card")

    newCard = document.getElementById("card").cloneNode(true);
    feeds.appendChild(newCard)

    newCard = document.getElementById("card")
    newCard.classList.remove("d-none");
    newCard.id = "card" + hash

    newBookmark = document.getElementById("bookmark")
    newBookmark.id = hash
    newBookmark.addEventListener("click", addToBookmark);

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
    newDatePosted.innerHTML = data.publishedAt

}


function addToBookmark(e) {
    e = e || window.event;
    e = e.target || e.srcElement;
    var hash = ""
    if (e.nodeName === 'BUTTON') {
        hash = e.id
        feedCard = document.getElementById("card" + e.id)

        alert(document.getElementById("title" + e.id).innerText)
        cardData = {
            'title': document.getElementById("title" + e.id).innerText,
            'author': document.getElementById("author" + e.id).innerText,
            'content': document.getElementById("content" + e.id).innerText,
            'urlToImage': document.getElementById("image" + e.id).src,
            'description': document.getElementById("description" + e.id).innerText,
            'publishedAt': document.getElementById("date-posted" + e.id).innerText,
            'url': document.getElementById("bibliography" + e.id).href
        }
    }
    feedCard.parentNode.removeChild(feedCard);
    console.log(cardData)
}

function getFeeds() {
    var url = 'https://newsapi.org/v2/top-headlines?' +
        'country=in&' +
        'apiKey=fb1c2caa84c441d890f12f20499c4604';
    var req = new Request(url);
    fetch(req)
        .then(response => response.json())
        .then(data => {
            for (feed in data.articles) {
                fetch(addCard(data.articles[feed], feed))
                    .then(res => {
                        console.log(data.articles[feed].author)
                    });
            }
        });
}



// var url = 'https://newsapi.org/v2/everything?' +
// 'q=Apple&' +
// 'from=2019-10-20&' +
// 'sortBy=popularity&' +
// 'laguage=en&'+
// 'apiKey=fb1c2caa84c441d890f12f20499c4604';

// var req = new Request(url);

// fetch(req)
// .then(response => response.json())
//     .then(data => {
//         for(feed in data.articles){
//             fetch(addCard(data.articles, feed))
//             .then(res => {console.log(data.articles[feed].author)});
//         }
// });