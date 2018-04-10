
    $('#create_note').submit(function(e){
        e.preventDefault();
        console.log('Sending Ajax request to', $(this).attr('action'));
        console.log('Submitting the following data', $(this).serialize());
        $.ajax({
            url: $(this).attr('action'), /* Where should this go? */
            method: 'post', /* Which HTTP verb? */
            data: $(this).serialize(), /* Any data to send along? */
            success: function(response) {
                console.log(response); /* What code should we run when the server responds? */
                $('#all_notes').html(renderNotes(response))
            }
        })
        $(this).reset();
    })
    $().ready(function(){
        $.ajax({
            url: '/initialize',
            method: 'get',
            success: function(response){
                $('#all_notes').html(renderNotes(response))
            }
        })
    })
function renderNotes(notes){
    var el = document.createElement('div');
    for(post in notes){
        var n = document.createElement('div');
        n.setAttribute('class', 'note');
        t = document.createElement('h4');
        t.innerText = notes[post].fields.content;
        n.appendChild(t);
        el.appendChild(n);
    }
    return el
}
