async function submitAndClickCorrectOption() {
    const question = document.querySelector("#questionSpan").innerText;
    const options = [];
    document.querySelectorAll(".OptionText").forEach((option) => {
        options.push(option.innerText);
    });

    const optButtons = document.getElementsByTagName("mat-radio-button");

    try {
        const response = await fetch("http://localhost:8080", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ question, options }),
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const result = await response.json();
        const message = result.response.replace(/\n/g, " ");
        const correctOptionIndex = parseInt(message, 10) - 1;
        alert(`Correct option index: ${options[correctOptionIndex]} (${correctOptionIndex + 1})`);


        if (correctOptionIndex >= 0 && correctOptionIndex < optButtons.length) {
            optButtons[correctOptionIndex].click();
        } else {
            console.error("Invalid response or option index out of range");
        }
    } catch (error) {
        console.error("An error occurred:", error);
    }
}

document.querySelector("#questionSerialNo").addEventListener("click", submitAndClickCorrectOption);