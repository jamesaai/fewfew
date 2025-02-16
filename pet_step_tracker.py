load("render.star", "render")
load("http.star", "http")

# Replace with your actual username, password, and pet ID
VAR_USERNAME = "emailaddress@gmail.com"
VAR_PASSWORD = "password"
VAR_PET_ID = "petid"

API_BASE_URL = "https://api.tryfi.com"
API_LOGIN_URL = API_BASE_URL + "/auth/login"
API_GRAPHQL = API_BASE_URL + "/graphql"

# GraphQL query for pet device details
QUERY_PET_DEVICE_DETAILS = """
{
  pet (id: \"""" + VAR_PET_ID + """\") {
    name
    dailyStat: currentActivitySummary (period: DAILY) {
      totalSteps
      stepGoal
    }
  }
}
"""

def authenticate_user():
    """Authenticate user and return session ID and cookie."""
    try:
        resp = http.post(API_LOGIN_URL, json_body={"email": VAR_USERNAME, "password": VAR_PASSWORD})
        resp.raise_for_status()  # Raise an exception for HTTP errors
        session_id = resp.json().get("sessionId")
        cookie = resp.headers.get("Set-Cookie")
        return session_id, cookie
    except Exception as e:
        print(f"Error authenticating user: {e}")
        return None, None

def fetch_pet_data(session_id, cookie):
    """Fetch pet activity data using the provided session ID and cookie."""
    try:
        resp = http.post(API_GRAPHQL, headers={"sessionId": session_id, "Cookie": cookie}, json_body={"query": QUERY_PET_DEVICE_DETAILS})
        resp.raise_for_status()
        data = resp.json().get("data")
        pet_name = data["pet"]["name"]
        daily_steps = data["pet"]["dailyStat"]["totalSteps"]
        step_goal = data["pet"]["dailyStat"]["stepGoal"]
        return pet_name, daily_steps, step_goal
    except Exception as e:
        print(f"Error fetching pet data: {e}")
        return None, None, None

def main():
    # Authenticate user
    session_id, cookie = authenticate_user()
    if not session_id or not cookie:
        return render.Root(child=render.Text("Authentication failed"))

    # Fetch pet data
    pet_name, daily_steps, step_goal = fetch_pet_data(session_id, cookie)
    if not pet_name:
        return render.Root(child=render.Text("Failed to fetch pet data"))

    # Render pet data
    return render.Root(
        child=render.Text(f"{pet_name}\n{int(daily_steps)}/{int(step_goal)} steps")
    )

