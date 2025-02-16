const getDogSteps = async () => {
  const url = "https://api.tryfi.com/auth/login";  // Placeholder URL
  const headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN", // You'll need to get this from the API
    "Content-Type": "application/json"
  };

  try {
    const response = await fetch(url, { method: 'GET', headers });
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error fetching dog steps:", error);
  }
};
