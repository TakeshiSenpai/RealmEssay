import { render } from '@react-email/components';
import nodemailer from 'nodemailer';
import CodigoDeTarea from "../emails/CodigoDeTarea.jsx";


export async function sendEmail (to, validationCode){

const transporter = nodemailer.createTransport({
  host: 'smtp.forwardemail.net',
  port: 465,
  secure: true,
  auth: {
    user: 'realmessay@gmail.com',
    pass: 'ssoo epjf yzfd peya',
  },
});

const emailHtml = await render(<CodigoDeTarea validationCode={validationCode} />);

const options = {
  from: 'you@example.com',
  to: to,
  subject: 'hello world',
  html: emailHtml,
};

await transporter.sendMail(options , (error, infor)=>{
  if(error) return console.log(error);
  return console.log("Correo enviado");
});

}


