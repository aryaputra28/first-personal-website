$(document).ready(function() {
    cariBuku("happy");
    // $("#searchButton").click(function(){
    //     var pencarian = $("#searchArea").val();
    //     cariBuku(pencarian);
    //     console.log("yang dicari = " + pencarian);
    // })
    $("input").keyup(
        function(){
            var pencarian = $("#searchArea").val();
            cariBuku(pencarian);
        }
    )
});

cariBuku = (search_value) => {
    $.ajax({
        type:"GET",
        url: buku_url + search_value,
        dataType: "json",
        timeout: 500,
        success: function(data) {
            $('#list_books').empty();
            for (item of data.items) {
                console.log(item.volumeInfo);
                var author = item.volumeInfo.authors;
                if (author == undefined ) {
                    author = "Tidak Ditemukan"
                } else {
                    author =item.volumeInfo.authors[0];
                }
                var deskripsi = item.volumeInfo.description ? item.volumeInfo.description.substr(0,300)+"..." : "Deskripsi Tidak ada";
                var title = item.volumeInfo.title ? item.volumeInfo.title : "";
                var img = item.volumeInfo.imageLinks.smallThumbnail;
                if (!img) {
                    img = item.volumeInfo.imageLinks.smallThumbnail;
                } else if (!img) {
                    img = "https://www.freeiconspng.com/uploads/no-image-icon-8.png";
                }
                var linkBaca = item.volumeInfo.previewLink ? item.volumeInfo.previewLink : "";
                var tanggal = item.volumeInfo.publishedDate  ? item.volumeInfo.publishedDate : "";
                var result = '<div class="d-flex bookCard" style="padding: 15px; background-color: #3E4D5E; border-radius:20px"><img src=' +img + 'height="195px" width="128px" style="margin: 0 30px 0 0"><div style="color: white;"><h3 >'+title+'</h3><h6>' + tanggal+ '</h6><h6>Author : '+author+'</h6><p>' + deskripsi + '</p><a type="button" class="btn btn-primary" href= '+ linkBaca +'>Read</a></div></div><div style="height: 50px;"></div>'
                $("#list_books").append(result);
            }
        }
    })
}