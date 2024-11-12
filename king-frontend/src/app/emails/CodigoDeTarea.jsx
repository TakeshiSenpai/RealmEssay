import {
    Body,
    Container,
    Head,
    Heading,
    Html,
    Img,
    Link,
    Section,
    Text,
  } from "@react-email/components";
  import React from "react";
  
  const baseUrl = process.env.VERCEL_URL
    ? `https://${process.env.VERCEL_URL}`
    : " https://avatars.githubusercontent.com/u/124811814?v=4 ";
  
  const homeworkCode = ({ validationCode }) => (
    <Html>
      <Head />
      <Body style={main}>
        <Container style={container}>
          <Img
            src={`${baseUrl}/static/plaid-logo.png`}
            width="212"
            height="88"
            alt="Plaid"
            style={logo}
          />
          <Text style={tertiary}>Código de tarea </Text>
          <Heading style={secondary}>
            Ingresa el código en el apartado para subir tu tarea
          </Heading>
          <Section style={codeContainer}>
            <Text style={code}>{validationCode}</Text>
          </Section>
          <Text style={paragraph}>¿No esperabas este email?</Text>
          <Text style={paragraph}>
            Contáctanos{" "}
            <Link href="mailto:realmessay@gmail.com" style={link}>
              realmessay@gmail.com
            </Link>{" "}
          </Text>
        </Container>
       </Body>
    </Html>
  );
  
  homeworkCode.PreviewProps = {
    validationCode: "144833",
  };
  
  export default homeworkCode;
  
  const main = {
    backgroundColor: "#ffffff",
    fontFamily: "HelveticaNeue,Helvetica,Arial,sans-serif",
  };
  
  const container = {
    backgroundColor: "#ffffff",
    border: "1px solid #eee",
    borderRadius: "5px",
    boxShadow: "0 5px 10px rgba(20,50,70,.2)",
    marginTop: "20px",
    maxWidth: "360px",
    margin: "0 auto",
    padding: "68px 0 130px",
  };
  
  const logo = {
    margin: "0 auto",
  };
  
  const tertiary = {
    color: "#0a85ea",
    fontSize: "11px",
    fontWeight: 700,
    fontFamily: "HelveticaNeue,Helvetica,Arial,sans-serif",
    height: "16px",
    letterSpacing: "0",
    lineHeight: "16px",
    margin: "16px 8px 8px 8px",
    textTransform: "uppercase",
    textAlign: "center",
  };
  
  const secondary = {
    color: "#000",
    display: "inline-block",
    fontFamily: "HelveticaNeue-Medium,Helvetica,Arial,sans-serif",
    fontSize: "20px",
    fontWeight: 500,
    lineHeight: "24px",
    marginBottom: "0",
    marginTop: "0",
    textAlign: "center",
  };
  
  const codeContainer = {
    background: "rgba(0,0,0,.05)",
    borderRadius: "4px",
    margin: "16px auto 14px",
    verticalAlign: "middle",
    width: "280px",
  };
  
  const code = {
    color: "#000",
    display: "inline-block",
    fontFamily: "HelveticaNeue-Bold",
    fontSize: "32px",
    fontWeight: 700,
    letterSpacing: "6px",
    lineHeight: "40px",
    paddingBottom: "8px",
    paddingTop: "8px",
    margin: "0 auto",
    width: "100%",
    textAlign: "center",
  };
  
  const paragraph = {
    color: "#444",
    fontSize: "15px",
    fontFamily: "HelveticaNeue,Helvetica,Arial,sans-serif",
    letterSpacing: "0",
    lineHeight: "23px",
    padding: "0 40px",
    margin: "0",
    textAlign: "center",
  };
  
  const link = {
    color: "#444",
    textDecoration: "underline",
  };
  
  const footer = {
    color: "#000",
    fontSize: "12px",
    fontWeight: 800,
    letterSpacing: "0",
    lineHeight: "23px",
    margin: "0",
    marginTop: "20px",
    fontFamily: "HelveticaNeue,Helvetica,Arial,sans-serif",
    textAlign: "center",
    textTransform: "uppercase",
  };
  