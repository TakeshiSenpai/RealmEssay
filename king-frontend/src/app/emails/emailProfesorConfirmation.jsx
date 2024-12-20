import {
    Body,
    Container,
    Column,
    Head,
    Hr,
    Html,
    Img,
    Link,
    Preview,
    Row,
    Section,
    Text,
  } from "@react-email/components";
  import * as React from "react";
  
  const baseUrl = process.env.VERCEL_URL
    ? `https://${process.env.VERCEL_URL}`
    : "https://avatars.githubusercontent.com/u/124811814?v=4";
  
  const EmailProfesorConfirmation = ({textRubric, textHomework, profesor}) => (
    <Html>
      <Head />
      <Preview>Real Essay tarea creada resumen</Preview>
      <Body style={main}>
        <Container style={container}>
          <Section>
            <Row>
              <Column>
                <Img
                  style={headerBlue}
                  src={`${baseUrl}/static/google-play-header.png`}
                  width="305"
                  height="28"
                  alt="Google Play developers header blue transparent"
                />
                <Img
                  style={sectionLogo}
                  src={`${baseUrl}/static/google-play-logo.png`}
                  width="155"
                  height="31"
                  alt="Google Play"
                />
              </Column>
            </Row>
          </Section>
    
          <Section style={paragraphContent}>
            <Hr style={hr} />
            <Text style={heading}>Aviso de creación de tarea</Text>
            <Text style={paragraph}>Hola profesor, {profesor}</Text>
            <Text style={paragraph}>
              Aquí esta un resumen de su tarea creada
            </Text>
                
          </Section>
          <Section style={paragraphList}>
            <Text style={paragraph}>
                {textHomework}  
            </Text>
          </Section>
          <Section style={paragraphContent}>
            <Text style={paragraph}>
                Prompt de la rúbrica enviado a la IA: {textRubric}  
            </Text>
            <Hr style={hr} />
          </Section>
  
          <Section style={paragraphContent}>
            <Text style={paragraph}>Gracias,</Text>
            <Text style={{ ...paragraph, fontSize: "20px" }}>
              Realm Essay
            </Text>
          </Section>
  
          <Section style={paragraphContent}>
            
              <Text style={paragraph}>Contáctanos <br/>
               <Link href="mailto:realmessay@gmail.com" style={link}>
                    realmessay@gmail.com
                </Link>{" "}
                </Text>
          </Section>
  
          <Section style={{ ...paragraphContent, paddingBottom: 30 }}>
            <Text
              style={{
                ...paragraph,
                fontSize: "12px",
                textAlign: "center",
                margin: 0,
              }}
            >
              © 2024 Princess Development S.A de C.V, Blvd. Benito Juárez, 
              Insurgentes Este, 21280 Mexicali, B.C. 
            </Text>
            <Text
              style={{
                ...paragraph,
                fontSize: "12px",
                textAlign: "center",
                margin: 0,
              }}
            >
              Usted recibió este anuncio por correo eléctronico de manera automática para informale
              de la creacion de su tarea.
            </Text>
          </Section>
        </Container>
      </Body>
    </Html>
  );
  
  export default EmailProfesorConfirmation
  const main = {
    backgroundColor: "#dbddde",
    fontFamily:
      '-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif',
  };
  
  const sectionLogo = {
    padding: "0 40px",
  };
  
  const headerBlue = {
    marginTop: "-1px",
  };
  
  const container = {
    margin: "30px auto",
    backgroundColor: "#fff",
    borderRadius: 5,
    overflow: "hidden",
  };
  
  const containerContact = {
    backgroundColor: "#f0fcff",
    width: "90%",
    borderRadius: "5px",
    overflow: "hidden",
    paddingLeft: "20px",
  };
  
  const heading = {
    fontSize: "14px",
    lineHeight: "26px",
    fontWeight: "700",
    color: "#004dcf",
  };
  
  const paragraphContent = {
    padding: "0 40px",
  };
  
  const paragraphList = {
    paddingLeft: 40,
  };
  
  const paragraph = {
    fontSize: "14px",
    lineHeight: "22px",
    color: "#3c4043",
  };
  
  const link = {
    ...paragraph,
    color: "#004dcf",
  };
  
  const hr = {
    borderColor: "#e8eaed",
    margin: "20px 0",
  };
  
  const footer = {
    maxWidth: "100%",
  };
  