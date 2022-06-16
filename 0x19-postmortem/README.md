<!-- omit in toc -->
# POSTMORTEM

<!-- omit in toc -->
## Table of Content
- [Issue Summary](#issue-summary)
- [Timeline](#timeline)
- [Root cause and Resolution](#root-cause-and-resolution)
- [Corrective and Preventive measures](#corrective-and-preventive-measures)


## Issue Summary
There was a service downtime between 8:45 pm WAT and 9:23 pm WAT on January 5th, 2022.  
The effect was mainly on the pharmacy interface. Healthcare personnel were not able to make prescription requests to the pharmacy. All personnel were affected.  
The cause of the downtime was traced to a bug introduced by the API update of December 2021. The bug was triggered by onboarding drugs whose name contains non-ASCII characters.

## Timeline
- **8:45 pm WAT** - Issue was noticed.
- **8:50 pm WAT** - complaint was made to the IT front desk by the pharmacist on call while trying to enter newly acquired drugs into the pharmacy store.
- **8:55 pm WAT** -personnel thought it was a network-related error and proceeded to refresh the browser page multiple times, noting that other aspects of the service were up but the issue persisted.
- **9:02 pm WAT** - The incident was reported to the IT front desk officer who promptly placed a call to the IT officer on call (Terence Waller).
- **9:10 pm** - Since other microservices were not affected and the issue was seen to be specific to pharmacy-related requests, the debug mode was turned on which revealed where the error was.
- **9:20 pm WAT** - The incident was mitigated by reverting the current API version to the previous one and restarting the pharmacy microservice. This is to allow for a more rigorous review of the recent update and to fix other potential errors yet to surface.
- **9:23 pm WAT** - Service is back up.

## Root cause and Resolution
As stated above, the root cause of the downtime was traced to a bug in the pharmacy API introduced by the last update from API version `0.2.6` to `0.3.0`. The bug was found in the file at /api/views/pharmacy/drugs.py on line 254 in view function add_drugs(details). The character encoding was not passed to the open function writing to a temporary drug file.  

![Bug Image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/scjeufmmq9f14jqrz3op.png)

The issue was fixed by starting the backup service running on API version `0.2.6`, isolating the current version to allow for a more extensive investigation into it when the team assembles.

## Corrective and Preventive measures
- set `debug=True` on the flask server start-up command
- restart the server.
- replicate the issue by sending a drug request with a non-ASCII character in the name.
- print the debug output and save the traceback to an error.txt file.
- extract the server access and error logs
- shut down the current server based on the current API
- start up the backup server running on API version `0.2.6`
- repeat the same request

Improvements need to be made in the code review process. Adding more automated tests to cover some extraneous scenarios will help with spotting such errors in the future. Using a strict mode for the codebase is another way to mitigate such issues.