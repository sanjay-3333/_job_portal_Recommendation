document.getElementById("recommendationForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const user_id = parseInt(document.getElementById("user_id").value);
  const skills = document.getElementById("skills").value.split(",").map(s => s.trim());
  const top_n = parseInt(document.getElementById("top_n").value);

  try {
    const response = await fetch("http://127.0.0.1:8000/recommend/collab/recommend/hybrid", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id, skills, top_n })
    });

    const result = await response.json();
    document.getElementById("output").textContent = JSON.stringify(result, null, 2);
  } catch (err) {
    document.getElementById("output").textContent = "Error: " + err.message;
  }
});
