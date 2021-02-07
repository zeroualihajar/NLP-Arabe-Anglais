import { LoginService } from './../login/login.service';
import { Injectable } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';
import {formatDate} from '@angular/common';

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

  constructor(private apollo: Apollo, private loginService:LoginService) { }

  serv: String ="";
  res: any;
  rslt: any;

  add(form: FormGroup){


      this.apollo.mutate({
        mutation: addText,
        variables: {
          content: form.value.myText,
          // id: LoginService.id,
          id: "601c86aaefcf8f34d720b443",
          nameOp:form.value.checkArray
        }
      }).subscribe(({data}) => {
        this.res = data
        let l = this.res['addText']['user']['text'].length
        let k = this.res['addText']['user']['text'][l-1]['operation'].length

        let content = this.res['addText']['user']['text'][l-1]['operation'][k-1]['resultOp']
        console.log(content)
        this.rslt = content
      },
      () => console.error('Error : ', Error))
  }
}
