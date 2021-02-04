import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ServicesNlpComponent } from './services-nlp.component';

describe('ServicesNlpComponent', () => {
  let component: ServicesNlpComponent;
  let fixture: ComponentFixture<ServicesNlpComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ServicesNlpComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ServicesNlpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
