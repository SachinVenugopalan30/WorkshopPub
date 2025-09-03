from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI(
    title="LeetCode to Production",
    description="A demo microservice that exposes LeetCode problems as APIs",
    version="1.0.0",
)

class TwoSumRequest(BaseModel):
    nums: List[int]
    target: int

class TwoSumResponse(BaseModel):
    results: Optional[List[int]] = None
    error: Optional[str] = None

@app.post("/two_sum")
def two_sum(req: TwoSumRequest):
    '''
        Used to find the index of two numbers in an array if they sum up to a target input
    '''
    nums_dict = {}
    nums = req.nums
    target2 = req.target
    for i in range(len(nums)):
        if nums_dict.get(target2 - nums[i]) == None:
            nums_dict[nums[i]] = i
        else:
            return [nums_dict.get(target2 - nums[i]), i]


# Define request schema: 
# It’s how you define the shape of the data your API expects

# Valid Request:
# {
#   "nums": [2, 7, 11, 15],
#   "target": 9
# }

# 400 Bad Request:
# {
#   "nums": "not a list",
#   "target": "hello"
# }

# class TwoSumRequest(BaseModel):
#     nums:
#     target:



# Define response schema: 
# It defines the shape of the data your API will return

# Example when a solution exists:

# {
#   "result":
#   "error":
# } 

# class TwoSumResponse(BaseModel):
#     result: 
#     error:


# FastAPI route handler / endpoint function

# @app.post("/two_sum", response_model=TwoSumResponse)
# Whenever someone sends a POST request to the path /two_sum, run the function below

# def two_sum(req: TwoSumRequest):
#     """Solve the Two Sum problem as an API endpoint"""

    # Add your LeetCode Logic in here!
    
    # return {"error": "No two sum solution found"}