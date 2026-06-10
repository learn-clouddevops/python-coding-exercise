'''Given a list of deployment dicts, return:
- total_deployments: count of all deployments
- successful: count where status == "success"
- failed_apps: list of app names where 
               status == "failed", sorted
- success_rate: percentage of successful 
                deployments rounded to 1 decimal
                e.g. 3 out of 5 = 60.0
- most_deployed: app name that appears 
                 most times in the list

Input:
deployments = [
    {"app": "frontend", "status": "success", "env": "prod"},
    {"app": "backend",  "status": "failed",  "env": "prod"},
    {"app": "frontend", "status": "success", "env": "dev"},
    {"app": "backend",  "status": "success", "env": "dev"},
    {"app": "frontend", "status": "failed",  "env": "prod"},
    {"app": "orders",   "status": "success", "env": "prod"},
]

Expected:
{
    "total_deployments": 6,
    "successful": 4,
    "failed_apps": ["backend", "frontend"],
    "success_rate": 66.7,
    "most_deployed": "frontend"
}

Edge cases:
- empty list → return {}
- all successful → failed_apps = []'''

deployments = [
    {"app": "frontend", "status": "success", "env": "prod"},
    {"app": "backend",  "status": "failed",  "env": "prod"},
    {"app": "frontend", "status": "success", "env": "dev"},
    {"app": "backend",  "status": "success", "env": "dev"},
    {"app": "frontend", "status": "failed",  "env": "prod"},
    {"app": "orders",   "status": "success", "env": "prod"},
]



######################################################################
def deployment_calculate(deployments):

    successful =[]
    failed=[]
    most_deployed={}
 

    
    if not deployments:
            return {}

    for deploy in deployments:
            if deploy["status"] == "success":
                successful.append(deploy["app"])

                
            if deploy["status"] != "success":
                failed.append(deploy["app"])  

            app = deploy["app"]
            most_deployed[app] = most_deployed.get(app,0) + 1



    return {
    "total_deployments": len(deployments),
    "successful": len(successful),
    "failed_apps": sorted(set(failed)),
    "success_rate": round(len(successful) / len(deployments) *100 ,2),
    "most_deployed": max(most_deployed, key=lambda x: most_deployed[x])
}



result = deployment_calculate(deployments)
print(result)
