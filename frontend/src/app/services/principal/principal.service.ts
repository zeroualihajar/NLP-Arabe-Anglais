import { LoginService } from './../login/login.service';
import { Injectable } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';
import {formatDate} from '@angular/common';

// const addOp = gql`
//   mutation AddOp($content: String!, $type: String!, $dateCr: Date!, $nameOp: String!, $dateOp: Date!, $id: String!)
//   {
//     addOp(content: $content, type: $type , dateCr: $dateCr, nameOp: $nameOp, dateOp: $dateOp, id: $id)
//     {
//       text
//       {
//         content,
//         type,
//         dateCr,
//         operation {
//           nameOp,
//           dateOp,
//           user {
//             id
//           }
//         }
//       }

//     }
// }
// `;





const addText = gql`
  mutation AddText($content: String!, $id: String!, $nameOp: String!)
  {
    addText(content: $content, id: $id, nameOp: $nameOp)
    {

        user
          {
            id,
            text
            {
              content,
              operation
              {
                nameOp
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
  add(form: FormGroup){

    // console.log(LoginService.id)
    // console.log(form.value.myText)

    for (var val of form.value.checkArray)
    {
      // this.serv += val
      // this.serv += "-"
      this.serv = val
    }

      this.apollo.mutate({
        mutation: addText,
        variables: {
          content: form.value.myText,
          id: LoginService.id,
          nameOp:this.serv
        }
      }).subscribe(({data}) => {
        console.log('AddOperation : ', data)
      },
      () => console.error('Error : ', Error))
  }
}
