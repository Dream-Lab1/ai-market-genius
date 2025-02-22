document.getElementById("report-form").addEventListener("submit", function(event) {
    event.preventDefault();

    const businessName = document.getElementById("business-name").value;
    const industry = document.getElementById("industry").value;
    const transaction = document.getElementById("transaction").value;

    if (!businessName || !industry || !transaction) {
        alert("Please fill all fields.");
        return;
    }

    alert(`✅ Request received! Your AI Market Report for ${businessName} in ${industry} will be sent soon.`);
});
