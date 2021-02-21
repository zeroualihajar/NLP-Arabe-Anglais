import { LoginService } from './../login/login.service';
import { Injectable } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';
import {formatDate} from '@angular/common';
import { LoginComponent } from 'src/app/pages/login/login.component';

const addText = gql`
  mutation AddText($content: String!, $id: String!, $nameOp: String!)
  {
    addText(content: $content, id: $id, nameOp: $nameOp)
    {
      user
      {
        text
        {
          operation
          {
            resultOp
          }
        }
      }
    }
  }
`;

@Injectable({
  providedIn: 'root'
})
export class PrincipalService {

  serv: String ="";
  res: any;
  rslt: any;
  l: any;
  k: any;
  ct: any;

  constructor(private apollo: Apollo) {}

  add(form: FormGroup){

    console.log("text : " + form.value.myText )
     this.apollo.mutate({
      mutation: addText,
      variables: {
        content: form.value.myText,
        id: LoginComponent.id,
        nameOp:form.value.checkArray
      }
    }).subscribe(({data}) => {
      console.log("text 2 ")
      this.res = data
      this.l = this.res['addText']['user']['text'].length
      this.k = this.res['addText']['user']['text'][this.l-1]['operation'].length

      this.ct = this.res['addText']['user']['text'][this.l-1]['operation'][this.k-1]['resultOp']

      this.rslt = this.ct
      console.log("data : "+this.rslt)
      }, (error) => {
        console.log('Error : ' , error)
      });
  }
}
