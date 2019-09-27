
## Each college with these details 
## College Item
{
    id: 'testCollege' + i,
    name: 'testCollege' + i,
    primaryContactJson: {
        "email": "testCollege" + i + "User" + i + "@test.com",
        "id": "testCollege" + i + "User" + i,
        "metadata": {
            "callerClientId": "7lm01o4mi8f8v61bjfljbhj0rp",
            "region": "us-east-1",
            "userPoolId": "us-east-1_MQ0aDB3ZL"
        },
        "name": "testCollege" + i + "User" + i,
        "organizationId": 'testCollege' + i,
        "organizationType": "college",
        "phoneNumber": "+919582819710",
        "userName": "college_testCollege" + i + "User" + i + "@test.com",
        "createdAt": new Date().toISOString(),
        "updatedAt": new Date().toISOString(),
    },
    status: "active",
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
}


{
                                "__typename": "drive",
                                "collegeId": 'testCollege' + i,
                                "endDate": "2019-08-22T00:00:00.000Z",
                                "id": "testCollege" + i + "Drive" + 1,
                                "name": "testCollege" + i + " Drive 1 '19-'20",
                                "startDate": "2019-06-13T00:00:00.000Z",
                                "type": "job",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }


{
                                "id": 'testCompany' + i,
                                "name": 'testCompany' + i,
                                "primaryContactJson": {
                                    "email": "testCompany" + i + "User" + i + "@test.com",
                                    "id": "testCompany" + i + "User" + i,
                                    "metadata": {
                                        "callerClientId": "7lm01o4mi8f8v61bjfljbhj0rp",
                                        "region": "us-east-1",
                                        "userPoolId": "us-east-1_MQ0aDB3ZL"
                                    },
                                    "name": "testCompany" + i + "User" + i,
                                    "organizationId": 'testCompany' + i,
                                    "organizationType": "company",
                                    "phoneNumber": "+919582819710",
                                    "userName": "company_testCompany" + i + "User" + i + "@test.com",
                                    createdAt: new Date().toISOString(),
                                    updatedAt: new Date().toISOString(),
                                },
                                "status": "active",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }

{
                                "email": "testCompany" + i + "User" + i + "@test.com",
                                "id": "testCompany" + i + "User" + i,
                                "metadata": {
                                    "callerClientId": "7lm01o4mi8f8v61bjfljbhj0rp",
                                    "region": "us-east-1",
                                    "userPoolId": "us-east-1_MQ0aDB3ZL"
                                },
                                "name": "testCompany" + i + "User" + i,
                                "organizationId": 'testCompany' + i,
                                "organizationType": "company",
                                "phoneNumber": "+919582819710",
                                "status": "enabled",
                                "userName": "company_testCompany" + i + "User" + i + "@test.com",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }
                        }

{
                                "email": "testCollege" + i + "User" + i + "@test.com",
                                "id": "testCollege" + i + "User" + i,
                                "metadata": {
                                    "callerClientId": "7lm01o4mi8f8v61bjfljbhj0rp",
                                    "region": "us-east-1",
                                    "userPoolId": "us-east-1_MQ0aDB3ZL"
                                },
                                "name": "testCollege" + i + "User" + i,
                                "organizationId": 'testCollege' + i,
                                "organizationType": "college",
                                "phoneNumber": "+919582819710",
                                "status": "enabled",
                                "updatedAt": new Date().toISOString(),
                                "userName": "college_testCollege" + i + "User" + i + "@test.com",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }
                        }


{
                                "__typename": "job",
                                "companyId": 'testCompany' + i,
                                "ctcJson": "{\"ctcMin\":100000,\"ctcMax\":100003,\"currency\":\"INR(Indian Rupee)\"}",
                                "description": "Full stack developer",
                                "id": "job1Company" + i,
                                "location": "Delhi",
                                "positionType": "Full Time",
                                "role": "Full stack developer",
                                "skills": "React",
                                "title": "Full Stack",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }
                        }
                        
                                                                      
module.exports = async (event, context, callback) => {
    console.log(`start time is - ${+ new Date()}`);
    ## insert 100 colleges, college users, companies and company users with 1 job per company

    for (var i = 1; i < 101; i++) {
        var batchParams = {
            RequestItems: {
                ['college-' + graphqlApiId + '-' + env]: [
                    {
                        PutRequest: {
                            Item: {
                                id: 'testCollege' + i,
                                name: 'testCollege' + i,
                                primaryContactJson: {
                                    "email": "testCollege" + i + "User" + i + "@test.com",
                                    "id": "testCollege" + i + "User" + i,
                                    "metadata": {
                                        "callerClientId": "7lm01o4mi8f8v61bjfljbhj0rp",
                                        "region": "us-east-1",
                                        "userPoolId": "us-east-1_MQ0aDB3ZL"
                                    },
                                    "name": "testCollege" + i + "User" + i,
                                    "organizationId": 'testCollege' + i,
                                    "organizationType": "college",
                                    "phoneNumber": "+919582819710",
                                    "userName": "college_testCollege" + i + "User" + i + "@test.com",
                                    "createdAt": new Date().toISOString(),
                                    "updatedAt": new Date().toISOString(),
                                },
                                status: "active",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }
                        }
                    }
                ],
                ['drive-' + graphqlApiId + '-' + env]: [
                    {
                        PutRequest: {
                            Item: {
                                "__typename": "drive",
                                "collegeId": 'testCollege' + i,
                                "endDate": "2019-08-22T00:00:00.000Z",
                                "id": "testCollege" + i + "Drive" + 1,
                                "name": "testCollege" + i + " Drive 1 '19-'20",
                                "startDate": "2019-06-13T00:00:00.000Z",
                                "type": "job",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }
                        }
                    },
                    // {
                    //     PutRequest: {
                    //         Item: {
                    //             "__typename": "drive",
                    //             "collegeId": 'testCollege' + i,
                    //             "endDate": "2019-08-22T00:00:00.000Z",
                    //             "id": "testCollege" + i + "Drive" + 2,
                    //             "name": "testCollege" + i + " Drive 2 '19-'20",
                    //             "startDate": "2019-06-13T00:00:00.000Z",
                    //             "type": "internship",
                    //             createdAt: new Date().toISOString(),
                    //             updatedAt: new Date().toISOString(),
                    //         }
                    //     }
                    // }
                ],
                ['company-' + graphqlApiId + '-' + env]: [
                    {
                        PutRequest: {
                            Item: {
                                "id": 'testCompany' + i,
                                "name": 'testCompany' + i,
                                "primaryContactJson": {
                                    "email": "testCompany" + i + "User" + i + "@test.com",
                                    "id": "testCompany" + i + "User" + i,
                                    "metadata": {
                                        "callerClientId": "7lm01o4mi8f8v61bjfljbhj0rp",
                                        "region": "us-east-1",
                                        "userPoolId": "us-east-1_MQ0aDB3ZL"
                                    },
                                    "name": "testCompany" + i + "User" + i,
                                    "organizationId": 'testCompany' + i,
                                    "organizationType": "company",
                                    "phoneNumber": "+919582819710",
                                    "userName": "company_testCompany" + i + "User" + i + "@test.com",
                                    createdAt: new Date().toISOString(),
                                    updatedAt: new Date().toISOString(),
                                },
                                "status": "active",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }
                        }
                    }
                ],
                ['user-' + graphqlApiId + '-' + env]: [
                    {
                        PutRequest: {
                            Item: {
                                "email": "testCompany" + i + "User" + i + "@test.com",
                                "id": "testCompany" + i + "User" + i,
                                "metadata": {
                                    "callerClientId": "7lm01o4mi8f8v61bjfljbhj0rp",
                                    "region": "us-east-1",
                                    "userPoolId": "us-east-1_MQ0aDB3ZL"
                                },
                                "name": "testCompany" + i + "User" + i,
                                "organizationId": 'testCompany' + i,
                                "organizationType": "company",
                                "phoneNumber": "+919582819710",
                                "status": "enabled",
                                "userName": "company_testCompany" + i + "User" + i + "@test.com",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }
                        }
                    },
                    {
                        PutRequest: {
                            Item: {
                                "email": "testCollege" + i + "User" + i + "@test.com",
                                "id": "testCollege" + i + "User" + i,
                                "metadata": {
                                    "callerClientId": "7lm01o4mi8f8v61bjfljbhj0rp",
                                    "region": "us-east-1",
                                    "userPoolId": "us-east-1_MQ0aDB3ZL"
                                },
                                "name": "testCollege" + i + "User" + i,
                                "organizationId": 'testCollege' + i,
                                "organizationType": "college",
                                "phoneNumber": "+919582819710",
                                "status": "enabled",
                                "updatedAt": new Date().toISOString(),
                                "userName": "college_testCollege" + i + "User" + i + "@test.com",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }
                        }
                    }
                ],
                ['job-' + graphqlApiId + '-' + env]: [
                    {
                        PutRequest: {
                            Item: {
                                "__typename": "job",
                                "companyId": 'testCompany' + i,
                                "ctcJson": "{\"ctcMin\":100000,\"ctcMax\":100003,\"currency\":\"INR(Indian Rupee)\"}",
                                "description": "Full stack developer",
                                "id": "job1Company" + i,
                                "location": "Delhi",
                                "positionType": "Full Time",
                                "role": "Full stack developer",
                                "skills": "React",
                                "title": "Full Stack",
                                createdAt: new Date().toISOString(),
                                updatedAt: new Date().toISOString(),
                            }
                        }
                    }
                ],
            }
        }

        var cognitoCollegeUserParams = {
            UserPoolId: userPoolId,
            Username: "college_testCollege" + i + "User" + i + "@test.com",
            TemporaryPassword: 'password1234',
            UserAttributes: [
                {
                    Name: "name",
                    Value: "testCollege" + i + "User" + i
                },
                {
                    Name: "phone_number",
                    Value: "+919582819710"
                },
                {
                    Name: "email",
                    Value: "testCollege" + i + "User" + i + "@test.com"
                },
                {
                    Name: "custom:group",
                    Value: 'college'
                },
                {
                    Name: "custom:collegeName",
                    Value: 'testCollege' + i,
                },
                {
                    Name: "custom:ddbId",
                    Value: "testCollege" + i + "User" + i,
                }
                /* more items */
            ],
        }

        var cognitoCompanyUserParams = {
            UserPoolId: userPoolId,
            Username: "company_testCompany" + i + "User" + i + "@test.com",
            TemporaryPassword: 'password1234',
            UserAttributes: [
                {
                    Name: "name",
                    Value: "testCompany" + i + "User" + i
                },
                {
                    Name: "phone_number",
                    Value: "+919582819710"
                },
                {
                    Name: "email",
                    Value: "testCompany" + i + "User" + i + "@test.com"
                },
                {
                    Name: "custom:group",
                    Value: 'company'
                },
                {
                    Name: "custom:companyName",
                    Value: 'testCompany' + i,
                },
                {
                    Name: "custom:ddbId",
                    Value: "testCompany" + i + "User" + i,
                }
                /* more items */
            ],
        }

        try {
            console.log(`start loop 1 with i ${i} - ${+ new Date()}`);
            //adding college
            //console.log(`batch inserting items - ${JSON.stringify(batchParams)}`);
            await documentClient.batchWrite(batchParams).promise();
            console.log('batch items inserted');

            //console.log(`creating college user in ddb with params - ${JSON.stringify(cognitoCollegeUserParams)}`);
            await cognitoidentityserviceprovider.adminCreateUser(cognitoCollegeUserParams).promise();
            console.log('college user in cognito created');

            try {
                //console.log(`creating company user in ddb with params - ${JSON.stringify(cognitoCompanyUserParams)}`);
                await cognitoidentityserviceprovider.adminCreateUser(cognitoCompanyUserParams).promise();
                console.log('company user in cognito created');
            }
            catch (err) {
                console.log(err);
            }

            console.log(`end loop 1 with i ${i} - ${+ new Date()}`);
        }

        catch (err) {
            console.log(err);
        }
    }

    //25 companies applies in 5 drives of 5 colleges
    for (var i = 1; i < 6; i++) {
        //looping over 5 colleges
        for (var j = 1; j < 26; j++) {
            //looping over 25 companies - adding jobOpening each
            //var status = Math.floor(Math.random() * 10) % 2 ? "active" : "pendingApproval";
            var status = "active";
            var batchCIDParams = {
                RequestItems: {
                    ['companyInDrive-' + graphqlApiId + '-' + env]: [
                        {
                            PutRequest: {
                                Item: {
                                    "__typename": "companyInDrive",
                                    "companyId": 'testCompany' + j,
                                    "driveId": "testCollege" + i + "Drive1",
                                    "id": "testCompanyInDrive-Company" + j + 'College' + i + 'drive1',
                                    "status": status,
                                    createdAt: new Date().toISOString(),
                                    updatedAt: new Date().toISOString(),
                                }
                            }
                        },
                        // {
                        //     PutRequest: {
                        //         Item: {
                        //             "__typename": "companyInDrive",
                        //             "companyId": 'testCompany' + j,
                        //             "driveId": "testCollege" + i + "Drive2",
                        //             "id": "testCompanyInDrive-Company" + j + 'College' + i + 'drive2',
                        //             "status": status == 'active' ? "active" : "pendingApproval",
                        //             createdAt: new Date().toISOString(),
                        //             updatedAt: new Date().toISOString(),
                        //         }
                        //     }
                        // }
                    ],
                    ['jobOpening-' + graphqlApiId + '-' + env]: [
                        {
                            PutRequest: {
                                Item: {
                                    "companyInDriveId": "testCompanyInDrive-Company" + j + 'College' + i + 'drive1',
                                    "ctcJson": "{\"ctcMin\":100000,\"ctcMax\":200000,\"currency\":\"INR(Indian Rupee)\"}",
                                    "description": "Full stack developer",
                                    "id": "jobOpening-Company" + j + 'College' + i + 'drive1',
                                    "jobId": "job1Company" + j,
                                    "location": "Delhi",
                                    "positionType": "Full Time",
                                    "requirements": "Do Well",
                                    "responsibilities": "Do Well",
                                    "role": "Full stack developer",
                                    "skills": "React, Mongo",
                                    "status": "verified",
                                    "title": "test",
                                    createdAt: new Date().toISOString(),
                                    updatedAt: new Date().toISOString(),
                                }
                            }
                        },
                        // {
                        //     PutRequest: {
                        //         Item: {
                        //             "companyInDriveId": "testCompanyInDrive-Company" + j + 'College' + i + 'drive2',
                        //             "ctcJson": "{\"ctcMin\":100000,\"ctcMax\":200000,\"currency\":\"INR(Indian Rupee)\"}",
                        //             "description": "Full stack developer",
                        //             "id": "jobOpening-Company" + j + 'College' + i + 'drive2',
                        //             "jobId": "job1Company" + j,
                        //             "location": "Delhi",
                        //             "positionType": "Full Time",
                        //             "requirements": "Do Well",
                        //             "responsibilities": "Do Well",
                        //             "role": "Full stack developer",
                        //             "skills": "React, Mongo",
                        //             "status": status == 'active' ? "active" : "pendingApproval",
                        //             "title": "test",
                        //             createdAt: new Date().toISOString(),
                        //             updatedAt: new Date().toISOString(),
                        //         }
                        //     }
                        // }
                    ],
                    ['round-' + graphqlApiId + '-' + env]: [
                        {
                            PutRequest: {
                                Item: {
                                    "canDelete": false,
                                    "canEdit": false,
                                    "id": "testRound1-Company" + j + 'College' + i + 'drive1',
                                    "isInterview": false,
                                    "jobOpeningId": "jobOpening-Company" + j + 'College' + i + 'drive1',
                                    "name": "Applications",
                                    "nextRound": "testRound2-Company" + j + 'College' + i + 'drive1',
                                    createdAt: new Date().toISOString(),
                                    updatedAt: new Date().toISOString(),
                                }
                            }
                        },
                        {
                            PutRequest: {
                                Item: {
                                    "canDelete": false,
                                    "canEdit": false,
                                    "id": "testRound2-Company" + j + 'College' + i + 'drive1',
                                    "isInterview": false,
                                    "jobOpeningId": "jobOpening-Company" + j + 'College' + i + 'drive1',
                                    "name": "Hired",
                                    "nextRound": "null",
                                    createdAt: new Date().toISOString(),
                                    updatedAt: new Date().toISOString(),
                                }
                            }
                        },
                        // {
                        //     PutRequest: {
                        //         Item: {
                        //             "canDelete": false,
                        //             "canEdit": false,
                        //             "id": "testRound1-Company" + j + 'College' + i + 'drive2',
                        //             "isInterview": false,
                        //             "jobOpeningId": "jobOpening-Company" + j + 'College' + i + 'drive2',
                        //             "name": "Applications",
                        //             "nextRound": "testRound2-Company" + j + 'College' + i + 'drive2',
                        //             createdAt: new Date().toISOString(),
                        //             updatedAt: new Date().toISOString(),
                        //         }
                        //     }
                        // },
                        // {
                        //     PutRequest: {
                        //         Item: {
                        //             "canDelete": false,
                        //             "canEdit": false,
                        //             "id": "testRound2-Company" + j + 'College' + i + 'drive2',
                        //             "isInterview": false,
                        //             "jobOpeningId": "jobOpening-Company" + j + 'College' + i + 'drive2',
                        //             "name": "Hired",
                        //             "nextRound": "null",
                        //             createdAt: new Date().toISOString(),
                        //             updatedAt: new Date().toISOString(),
                        //         }
                        //     }
                        // }
                    ],
                    ['student-' + graphqlApiId + '-' + env]: [
                        {
                            PutRequest: {
                                Item: {
                                    "__typename": "student",
                                    "credits": 0,
                                    "email": "testStudent" + j + 'College' + i + "@gmail.com",
                                    "id": "testStudent" + j + 'College' + i,
                                    "metadata": {
                                        "callerClientId": "7lm01o4mi8f8v61bjfljbhj0rp",
                                        "region": "us-east-1",
                                        "userPoolId": "us-east-1_MQ0aDB3ZL"
                                    },
                                    "name": "testStudent" + j + 'College' + i,
                                    "status": "enabled",
                                    "phoneNumber": "+919582819710",
                                    "userName": "student_" + "testStudent" + j + 'College' + i + "@gmail.com",
                                    createdAt: new Date().toISOString(),
                                    updatedAt: new Date().toISOString(),
                                }
                            }
                        }
                    ],
                    ['studentInDrive-' + graphqlApiId + '-' + env]: [
                        {
                            PutRequest: {
                                Item: {
                                    "driveId": "testCollege" + i + "Drive1",
                                    "id": "testStudentInDrive-testCollege" + i + "Drive1Student" + j,
                                    "registrationCode": (Math.floor(Math.random() * 10000)).toString(),
                                    "status": "active",
                                    "studentCollegeId": "testCollege" + i + "Student" + j,
                                    "studentId": "testStudent" + j + 'College' + i,
                                    "studentMail": "testStudent" + j + 'College' + i + "@test.com",
                                    "studentName": "testStudent" + j + 'College' + i,
                                    "studentPhone": "+919582819710",
                                    createdAt: new Date().toISOString(),
                                    updatedAt: new Date().toISOString(),
                                }
                            }
                        }
                    ],
                }
            }

            var cognitoStudentUserParams = {
                UserPoolId: userPoolId,
                Username: "student_" + "testStudent" + j + 'College' + i + "@gmail.com",
                TemporaryPassword: 'password1234',
                UserAttributes: [
                    {
                        Name: "name",
                        Value: "testStudent" + j + 'College' + i
                    },
                    {
                        Name: "phone_number",
                        Value: "+919582819710"
                    },
                    {
                        Name: "custom:group",
                        Value: 'student'
                    },
                    {
                        Name: "email",
                        Value: "testStudent" + j + 'College' + i + "@gmail.com"
                    },
                    {
                        Name: "custom:ddbId",
                        Value: "testStudent" + j + 'College' + i,
                    }
                ],
            }

            try {
                console.log(`start loop 2 with i - ${i}, j - ${j}`);

                //console.log(`creating companyInDrive with params - ${JSON.stringify(batchCIDParams)}`);
                await documentClient.batchWrite(batchCIDParams).promise();
                console.log('CID created');

                try {
                    //console.log(`creating student user in ddb with params - ${JSON.stringify(cognitoStudentUserParams)}`);
                    await cognitoidentityserviceprovider.adminCreateUser(cognitoStudentUserParams).promise();
                    console.log('student user in dbb created');
                }
                catch (err) {
                    console.log(err);
                }

                console.log(`end loop 2 with i - ${i}, j - ${j}`);
            }
            catch (err) {
                console.log(err);
            }
        }
    }

    //25 students of college 1 applies in first 5 companies
    for (var i = 1; i < 2; i++) {
        //looping over college
        for (var j = 1; j < 6; j++) {
            //looping over CID in college
            for (var k = 1; k < 26; k++) {
                //adding student applications CIDs
                var batchApplicationsParams = {
                    RequestItems: {
                        ['application-' + graphqlApiId + '-' + env]: [
                            {
                                PutRequest: {
                                    Item: {
                                        "id": "testApplication-Student" + k + 'College' + i + 'jobOpening' + j,
                                        "jobOpeningId": "jobOpening-Company" + j + 'College' + i + 'drive1',
                                        "nextApplicant": k != 25 ? "testApplication-Student" + (k + 1) + 'College' + i + 'jobOpening' + j : "null",
                                        "resumeOpeningId": "testResumeOpening-Student" + k + 'College' + i,
                                        "roundId": "testRound1-Company" + j + 'College' + i + 'drive1',
                                        "status": "applied",
                                        "studentInDriveId": "testStudentInDrive-testCollege" + i + "Drive1Student" + k,
                                        createdAt: new Date().toISOString(),
                                        updatedAt: new Date().toISOString(),
                                    }
                                }
                            }
                        ]
                    }
                }

                try {
                    console.log(`start loop 3 with i - ${i}, j - ${j}, k - ${k}`);
                    await documentClient.batchWrite(batchApplicationsParams).promise();
                    console.log('CID created');
                    console.log(`end loop 3`);
                }
                catch (err) {
                    console.log(err);
                }
            }
        }
    }

    console.log(`end time is - ${+ new Date()}`);
}