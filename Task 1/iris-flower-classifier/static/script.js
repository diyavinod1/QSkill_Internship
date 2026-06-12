async function predict(){

    let sl =
        document.getElementById("sl").value;

    let sw =
        document.getElementById("sw").value;

    let pl =
        document.getElementById("pl").value;

    let pw =
        document.getElementById("pw").value;

    if(
        !sl || !sw ||
        !pl || !pw
    ){
        alert(
            "Please fill all fields"
        );
        return;
    }

    const response =
    await fetch("/predict",{

        method:"POST",

        headers:{
            "Content-Type":
            "application/json"
        },

        body:JSON.stringify({

            sepal_length:sl,
            sepal_width:sw,
            petal_length:pl,
            petal_width:pw

        })
    });

    const data =
        await response.json();

    document
    .getElementById("result")
    .innerHTML =

    `
    <h2>${data.species}</h2>
    <p>
    Confidence:
    ${data.confidence}%
    </p>
    `;
}