
var trashes = document.querySelectorAll(".trash-icon");


function deleteNoteNow(card_id){
    var card = ".card-"+card_id
    var cardDiv = document.querySelector(card)

    cardDiv.style.display = "none"
}

for(let i = 0;i<trashes.length;i++){
    trashes[i].addEventListener("click",function(e){
        var card_id = this.getAttribute("id");
        var url = this.getAttribute("data-url")
      

        $.ajax({
            type:"POST",
            url:url,
            data:{
                "card_id":card_id,
                "csrfmiddlewaretoken":csrftoken
            },
            success:function(){
               
                deleteNoteNow(card_id)
            },
            error:function(e){
                console.log("error",e)
            }
        })

    })
}



/*problem -- today se ne updatea kada pozovem opet ovu funkcije jer se
            ne refresha stranica
*/


function getDate() {
    var now     = new Date(); 
    var year    = now.getFullYear();
    var month   = now.getMonth()+1; 
    var day     = now.getDate();
    var hour    = now.getHours();
    var minute  = now.getMinutes();

    if(month.toString().length == 1) {
         month = '0'+month;
    }
    if(day.toString().length == 1) {
         day = '0'+day;
    }   
    if(hour.toString().length == 1) {
         hour = '0'+hour;
    }
    if(minute.toString().length == 1) {
         minute = '0'+minute;
    }
     
    var dateTime = year+'-'+month+'-'+day+' '+hour+':'+minute   
    return dateTime;
}


function pushover(){
   
   var all_dates = document.querySelectorAll(".schedule-id");
   var today = getDate();
   for(let i=0;i<all_dates.length;i++){
       if(all_dates[i].innerText.includes(today)){
           var data_id = all_dates[i].getAttribute("data-id")
           var url = all_dates[i].getAttribute("data-url")

         $.ajax({
                 type:"POST",
                 url:url,
                 data:{
                     "data_id":data_id,
                     "csrfmiddlewaretoken":csrftoken
                 },
                 success:function(){
                     console.log("sending message with id",data_id," on",today,"...");
                 },
                 error:function(e){
                     console.log("badd")
                 }
                 
             })
         }
    
        }
        

       

}


var add_button = document.querySelector(".add-new-button") 

add_button.addEventListener("click",function(e){
    e.preventDefault()
    var form = document.querySelector(".note-form");
    var schedule = document.getElementById("id_schedule");
    var today = getDate();
    schedule.value = today;

    if(form.style.display !="flex"){
        form.style.display= "flex"
    }else{
        form.style.display = "none"
    }
})


window.onload = function(){
    pushover()
    setInterval(
        pushover(),60000 //1 min
    )
    
};  





