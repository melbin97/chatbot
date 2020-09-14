const submitButton = document.getElementById('submitButton')
const botInput = document.getElementById('botInput')
const botOutput = document.getElementById('botOutput')

submitButton.onclick = userSubmitEventHandler;
botInput.onkeyup = userSubmitEventHandler;

function userSubmitEventHandler(event)
{
    if((event.keyCode && event.keyCode==13)|| event.type=='click')
    {
        botOutput.innerText='Thinking....';
        askBot(botInput.value)
    }
}
function askBot(userInput) {
    const myRequest = new Request('/', {
        method: 'POST',
        body: userInput
    });

    fetch(myRequest).then(function(response) {
        if (!response.ok) {
            throw new Error('HTTP error, status = ' + response.status);
        } else {
            return response.text();
        }
    }).then(function(text) {
        botInput.value = '';
        botOutput.innerText = text;
    }).catch((err) => {
        console.error(err);
    });
}