import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Apollo, gql } from 'apollo-angular';
import { LoginComponent } from '../login/login.component';

const addEmotion = gql`
  mutation addEmotion($content: String!, $id: String!)
  {
    addEmotion(content: $content, id: $id)
    {
      user
      {
        text
        {
          emotion
        }
      }
    }
  }
`;

const addFake = gql`
  mutation addFake($content: String!, $id: String!)
  {
    addFake(content: $content, id: $id)
    {
      user
      {
        text
        {
          fakeNews
        }
      }
    }
  }
`;
@Component({
  selector: 'app-services-nlp',
  templateUrl: './services-nlp.component.html',
  styleUrls: ['./services-nlp.component.scss']
})
export class ServicesNlpComponent implements OnInit {

  form: FormGroup;
 result: any;

  serv: String ="";
  res: any;
  rslt: any;


  constructor(private fb: FormBuilder, private apollo: Apollo) {
  this.form = this.fb.group({
    myText: new FormControl('', Validators.required)
  })
}

  ngOnInit(): void {}

  submitForm(){
    console.log("text : " + LoginComponent.id )
     this.apollo.mutate({
      mutation: addEmotion,
      variables: {
        content: this.form.value.myText,
        id: LoginComponent.id,
      }
    }).subscribe(({data}) => {

      this.res = data

      let l = this.res['addEmotion']['user']['text'].length
      let k = this.res['addEmotion']['user']['text'][l-1]['emotion']

      this.result = k
      console.log("K : " +k)
      if(this.result == 1){
        this.result = "إيجابي"
      }
      else{
        this.result = "سلبي"
      }
      console.log("data : "+this.result)

      }, (error) => {
        console.log('Error : ' , error)
      });

  }

  fake(){

    console.log("text : " + LoginComponent.id )
     this.apollo.mutate({
      mutation: addFake,
      variables: {
        content: this.form.value.myText,
        id: LoginComponent.id,
      }
    }).subscribe(({data}) => {

      this.res = data
      console.log(this.res)
      let l = this.res['addFake']['user']['text'].length
      let k = this.res['addFake']['user']['text'][l-1]['fakeNews']
      this.result = k

      if(this.result == 1){
        this.result = "حقيقة"
      }
      else{
        this.result = "شائعة"
      }
      console.log("data : "+this.result)

      }, (error) => {
        console.log('Error : ' , error)
      });

  }
}
