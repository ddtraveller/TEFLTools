```
aws cloudformation create-stack \
  --stack-name ssl-cert-go-tl \
  --template-body file://ssl_cert_go_tl.yml \
  --parameters ParameterKey=DomainName,ParameterValue=go-tl.com \
  --region us-east-1
  
aws cloudformation create-stack \
  --stack-name go-tl-cloudfront-tl-tefl \
  --template-body file://cloudfront-distribution-tl-tefl.yml \
  --region us-west-2

aws cloudformation create-stack \
  --stack-name go-tl-cloudfront \
  --template-body file://cloudfront-distribution-tl-web.yml \
  --region us-west-2
```