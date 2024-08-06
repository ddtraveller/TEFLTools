There is a cloud front FUNCTION that is a part of the routing.
function handler(event) {
    var request = event.request;
    var headers = request.headers;
    var host = headers['host'].value;

    if (host === 'exams.go-tl.com') {
        // Route to Lambda
        request.origin = {
            custom: {
                domainName: 'ntg3qyh4r3xqq5dmate7vtljvm0tssff.lambda-url.us-west-2.on.aws',
                protocol: 'https',
                port: 443
            }
        };
    } else {
        // Route to S3 (default behavior)
        request.origin = {
            s3: {
                domainName: 'd36r6lbll727xz.cloudfront.net',
                region: 'us-west-2'
            }
        };
    }