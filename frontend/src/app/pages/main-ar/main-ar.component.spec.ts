import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MainArComponent } from './main-ar.component';

describe('MainArComponent', () => {
  let component: MainArComponent;
  let fixture: ComponentFixture<MainArComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MainArComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MainArComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
